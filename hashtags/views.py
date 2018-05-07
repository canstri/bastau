from django.shortcuts import render, redirect
from accounts.models import Profile
from news.models import Post
from courses.models import Course
from lectures.models import Lecture
from olymps.models import Olymp
from problems.models import Problem, CheckProblem

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from itertools import chain
from django.views.generic import ListView

def all_problems(request):
    array_of_user = []
    for prblm in Problem.objects.all():
        ht_array = []
        for hshtg in prblm.hashtag_list.all():
            ht_array.append(hshtg)
        array_of_user.append([prblm, CheckProblem.objects.get(user = request.user.id, problem_id = prblm.id), ht_array])    

    is_auth = False   
    profile = ''
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
        is_auth = True
 
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"

    context = {
        "staff":staff,
        "profile":profile,
        "array_of_user": array_of_user,
        "hashtag":'all',
        "is_auth":is_auth
    }
    return render(request, "problem_thread.html", context)




def problem_thread(request, hashtag):
    queryset = []
    for prblm in Problem.objects.all():
        for hshtg in prblm.hashtags:
            if hshtg == hashtag:
                queryset.append(prblm)

    array_of_user = []
    for prblm in queryset:
        ht_array = []
        for hshtg in prblm.hashtag_list.all():
            ht_array.append(hshtg)
        array_of_user.append([prblm, CheckProblem.objects.get(user = request.user.id, problem_id = prblm.id), ht_array])    

    is_auth = False   
    profile = ''
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
        is_auth = True
 
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"

    context = {
        "staff":staff,
        "profile":profile,
        "array_of_user": array_of_user,
        "hashtag":hashtag,
        "is_auth":is_auth
    }
    return render(request, "problem_thread.html", context)

