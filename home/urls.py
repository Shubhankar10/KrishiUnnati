


from django.urls.conf import include
from . import views
from .views import mainpage
from django.urls import include, path

urlpatterns = [
    path('', mainpage.as_view()),
    #path('index', views.index, name='index'),
    path('map', views.map, name='map'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('detail', views.detail, name='detail'),
]
