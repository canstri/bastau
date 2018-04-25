from django.shortcuts import render, redirect
from accounts.models import Profile
from news.models import Post
from courses.models import Course
from lectures.models import Lecture
from olymps.models import Olymp
from problems.models import Problem

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from itertools import chain
from django.views.generic import ListView




def main_view(request):
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
    
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"
    context = {
    	"staff":staff,
	    "user":request.user,
        "profile":profile,
    }
    return render(request, "main.html", context)

class SearchView(ListView):
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        profile = 'admin'
        if request.user.is_authenticated:
            profile = Profile.objects.get(user = request.user.id)
        
        staff = "no"
        if request.user.is_staff or request.user.is_superuser:
            staff = "yes"
        

        if query is not None:
            news_results = Post.objects.search(query)
            lesson_results = Lesson.objects.search(query)
            profile_results = Profile.objects.search(query)
            courses_results = Course.objects.search(query)
            problem_results = Problem.objects.search(query)

            # combine querysets 
            queryset_chain = chain(
                    problem_results,
                    news_results,
                    lesson_results,
                    profile_results,
                    courses_results,
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            context = {
                "staff":staff,
                "user":request.user,
                "profile":profile,
                "object_list":qs,
            }
            return render(request, "contacts.html", context)
        context = {
            "staff":staff,
            "user":request.user,
            "profile":profile,
            "object_list":Post.objects.none(),# just an empty queryset as default
        }
        return render(request, "contacts.html", context) 

def contacts_view(request):
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
    
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"
    context = {
        "staff":staff,
        "user":request.user,
        "profile":profile,
    }
    return render(request, "contacts.html", context)

def ratings_view(request):
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
    
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"


    queryset_list = Profile.objects.all()
    paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "staff":staff,
        "user":request.user,
        "profile":profile,
        "object_list": queryset,
    }
    return render(request, "ratings.html", context)
