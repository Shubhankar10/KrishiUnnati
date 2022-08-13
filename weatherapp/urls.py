from django.contrib import admin

from django.urls.conf import include
from . import views
from django.urls import include, path

urlpatterns = [
    path('weather',views.input,name='weather'),
    path('weatherresult', views.result, name='weatherresult'),
    

    
]