from django.conf.urls import url
from django.contrib import admin

from .views import (
    task_delete,
    )
from squads.views import ProblemAddAPIToggle

app_name = 'Enigmath'
urlpatterns = [
    url(r'^(?P<id>[\w-]+)/delete/$', task_delete, name='delete'),
    url(r'^api/(?P<slug>[\w-]+)/like/$', ProblemAddAPIToggle.as_view(), name='add-problem-api-toggle'),
]