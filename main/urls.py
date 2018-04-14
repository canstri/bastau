from django.conf.urls import url
from django.contrib import admin

from .views import (
    main_view,
    contacts_view,
    ratings_view,
    )

app_name = 'Enigmath'
urlpatterns = [
    url(r'^$', main_view, name='home'),
    url(r'^contacts/$', contacts_view, name='contacts'),
    url(r'^ratings/$', ratings_view, name='ratings'),
]