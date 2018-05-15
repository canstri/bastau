from urllib.parse import quote_plus

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import RedirectView

from .forms import SquadForm
from .models import Squad
from homeworks.models import Homework
from homeworks.forms import TaskForm
from problems.models import Problem, CheckProblem

from accounts.models import Profile

def squad_create(request):
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
        
    form = SquadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        print(instance)
        return HttpResponseRedirect(instance.get_absolute_url())
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"
    
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
    
    context = {
        "form": form,
        "staff":staff,
        "user":request.user,
        "profile":profile,
    }
    return render(request, "squad_create.html", context)

def squad_detail(request, slug=None):
    if not request.user.is_authenticated:
        raise Http404
    instance = get_object_or_404(Squad, slug=slug)
    share_string = quote_plus(instance.content)
    initial_data={
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }
    form = TaskForm(request.POST or None, initial=initial_data)
    if form.is_valid():
#        print(ContentType.objects.filter(model=form.cleaned_data.get("content_type"))[1])
        content_type = ContentType.objects.filter(model=form.cleaned_data.get("content_type"))[1]
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get("content")
        task_title = form.cleaned_data.get("title")
        new_task, created = Homework.objects.get_or_create(
                            content_type= content_type,
                            object_id = obj_id,
                            content = content_data,
                            title = task_title,
                        )
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"

    profile = 'admin'
    is_auth = False
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
        is_auth = True
     
    array_of_user = []
    for prblm in Problem.objects.all():
        ht_array = []
        for hshtg in prblm.hashtag_list.all():
            ht_array.append(hshtg)
        array_of_user.append([prblm, CheckProblem.objects.get(user = request.user.id, problem_id = prblm.id), ht_array])    

    context = {
        "title": "Groups",
        "instance": instance,
        "share_string": share_string,
        "squad_url":instance.get_absolute_url(),
        "staff":staff,
        "profile":profile,
        "user":request.user,
        "is_auth":is_auth,
        "form":form,
        "array_of_user": array_of_user,
        "hashtag":'all',
    }
    return render(request, "squad_detail.html", context)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class ProblemAddAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        # slug = self.kwargs.get("slug")
        obj = get_object_or_404(Homework, slug=slug)
        user = self.request.user
        
        data = {
            "like_num":0,
        }
        return Response(data)


def squad_list(request):
    if not request.user.is_authenticated:
        raise Http404

    queryset_list = Squad.objects.all()
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"
        queryset_list = Squad.objects.all()
    
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)

    squads = []
    for sq in queryset:
        in_squad = False
        for usr in sq.followers.all():
            if request.user == usr:
                in_squad = True
        squads.append([sq, in_squad])
        print(squads)
    
    context = {
        "object_list":queryset,
        "title": "Groups",
        "page_request_var": page_request_var,
        "staff" : staff,
        "profile": profile,
        "user":request.user,
        "squads":squads,
    }
    return render(request, "squad_list.html", context)





def squad_update(request, slug=None):
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Squad, slug=slug)
    form = SquadForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
        "user":request.user,
        "profile":profile,
    }
    return render(request, "squad_create.html", context)



def squad_delete(request, slug=None):
    try:
        instance = Squad.objects.get(slug=slug)
    except:
        raise Http404

    if not request.user.is_staff and not request.user.is_superuser:
        reponse.status_code = 403
        return HttpResponse("You do not have permission to do this.")


    if request.method == "POST":
        for task in instance.tasks:
            task.delete()
        instance.delete()
        messages.success(request, "Successfully deleted")
        return redirect("squads:list")
    context = {
        "object": instance
    }
    return render(request, "confirm_delete.html", context)


class GroupFollowToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Squad, slug=slug)
        user = self.request.user
        if user.is_authenticated:
            if user in obj.followers.all():
                obj.followers.remove(user)
                obj.followers_number -= 1
                obj.save()
            else:
                obj.followers.add(user)
                obj.followers_number += 1
                obj.save()
        return obj.get_list_url()

