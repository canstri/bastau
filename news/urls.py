from django.conf.urls import url
from django.contrib import admin

from .views import (
	news_list,
	news_create,
	news_detail,
	news_update,
	news_delete,
    PostLikeToggle,
    PostDisLikeToggle,
	)

app_name = 'Enigmath'
urlpatterns = [
	url(r'^$', news_list, name='list'),
    url(r'^create/$', news_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', news_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
    url(r'^(?P<slug>[\w-]+)/dislike/$', PostDisLikeToggle.as_view(), name='dislike-toggle'),
    url(r'^(?P<slug>[\w-]+)/edit/$', news_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', news_delete, name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]