from django.contrib import admin

from django.urls.conf import include
from . import views
from django.urls import include, path

urlpatterns = [
    
    path('wheather', views.wheather, name='wheather'),

]