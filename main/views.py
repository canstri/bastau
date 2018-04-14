from django.shortcuts import render, redirect
from accounts.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



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
