from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage),
    path('loginpage/',views.loginpage),
    path('insertuser/', views.insertuser,name='insertuser'),
    path('signuppage/', views.signup, name='signup'),
    path('basepage/', views.base, name='base'),
    path('basepage/aqi_result/', views.retrievedata, name='retrieve'),
]

