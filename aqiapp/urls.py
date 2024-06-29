from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import loginpage, insertuser, signup, base, retrievedata, home, get_air_quality_news

urlpatterns = [
    path('', views.home, name='home'),
    path('api/news/', get_air_quality_news, name='get_air_quality_news'),
    path('login/', views.loginpage, name='login'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('insertuser/', views.insertuser, name='insertuser'),
    path('signuppage/', views.signup, name='signup'),
    path('basepage/', views.base, name='base'),
    path('basepage/aqi_result/', views.retrievedata, name='retrieve'),
]

urlpatterns += staticfiles_urlpatterns()



