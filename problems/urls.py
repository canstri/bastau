from django.conf.urls import url
from django.contrib import admin

from .views import (
    problem_detail,
    problem_delete

    )

app_name = 'problems'
urlpatterns = [
    url(r'^(?P<id>\d+)/$', problem_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', problem_delete, name='delete'),
]