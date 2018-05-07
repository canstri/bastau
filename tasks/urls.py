from django.conf.urls import url
from django.contrib import admin

from .views import (
    task_delete,
    )

app_name = 'Enigmath'
urlpatterns = [
    url(r'^(?P<id>[\w-]+)/delete/$', task_delete, name='delete'),
]