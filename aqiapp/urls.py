from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.loginpage,name='login'),
    path('loginpage/',views.loginpage),
    path('insertuser/', views.insertuser,name='insertuser'),
    path('signuppage/', views.signup, name='signup'),
    path('basepage/', views.base, name='base'),
    path('basepage/aqi_result/', views.retrievedata, name='retrieve'),
]

