"""Defines urls for learning_logs app"""

from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
]