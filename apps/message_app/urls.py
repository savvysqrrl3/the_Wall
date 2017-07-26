from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'message_index'),
    url(r'^message$', views.message, name = 'message_posted'),
    url(r'^comment$', views.comment, name = 'comment_posted'),
]