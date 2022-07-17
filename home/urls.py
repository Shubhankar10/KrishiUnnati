
from django.contrib import admin

from django.urls.conf import include
from . import views
from django.urls import include, path

urlpatterns = [
    
    path('', views.home, name='home'),
    path('map', views.map, name='map'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('detail', views.detail, name='detail'),
    
]