from django.conf.urls import url
from django.contrib import admin

from .views import (
	account_view,
	)
from django.contrib.auth.models import User

app_name = 'accounts'
urlpatterns = [
    url(r'^(?P<user>[\w-]+)/$', account_view, name='profile'),
]