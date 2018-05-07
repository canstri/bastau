from django.conf.urls import url
from django.contrib import admin

from .views import (
    squad_list,
    squad_create,
    squad_detail,
    squad_update,
    squad_delete,
    GroupFollowToggle,
    )

app_name = 'Enigmath'
urlpatterns = [
    url(r'^$', squad_list, name='list'),
    url(r'^create/$', squad_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', squad_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/follow/$', GroupFollowToggle.as_view(), name='follow-toggle'),
    url(r'^(?P<slug>[\w-]+)/edit/$', squad_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', squad_delete, name='delete'),
]