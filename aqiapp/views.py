from django.shortcuts import render , redirect
from .models import cityairquality
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginpage(request):
    return render(request,  "website\loginpage.html")

def insertuser(request):
    vemail=request.POST['email']
    vusername=request.POST['username']
    vpassword = request.POST['password']
    us=User.objects.create_user(username=vusername,password=vpassword,email=vemail)
    us.save()
    return HttpResponse("Signup Successfull !!")
    
def signup(request):
    return render(request,"website/signuppage.html")  

def base(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("success")
            return render(request,'website/basepage.html')
        else:
            print("failure")
            message="Please try again"
            return render(request , "website/loginpage.html",{'login_page': message})

from django.db import connection

def retrievedata(request):
    if request.method == "POST":
        city_name = request.POST["city"]
        aqi_data = cityairquality.objects.filter(city_name=city_name).first()
        return render(request, 'website/datapage.html', {'aqi_data': aqi_data})
    else:
        return render(request, 'website/basepage.html')
    

