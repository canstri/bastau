from django.conf.urls import url
from django.contrib import admin

from .views import (
        problem_thread,
        all_problems,
        )

app_name = 'hashtags'
urlpatterns = [
    url(r'^all/', all_problems, name='all'),
    url(r'^(?P<hashtag>[\w-]+)/$', problem_thread, name='thread'), 
]