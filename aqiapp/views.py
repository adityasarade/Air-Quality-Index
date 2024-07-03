from django.shortcuts import render, redirect
from .models import cityairquality
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET
import requests

def loginpage(request):
    return render(request, "website/loginpage.html")

def logout_o(request):
    logout(request)
    return render(request, "website/loginpage.html")

def insertuser(request):
    if request.method == "POST":
        vemail = request.POST['email']
        vusername = request.POST['username']
        vpassword = request.POST['password']
        us = User.objects.create_user(username=vusername, password=vpassword, email=vemail)
        us.save()
        return HttpResponse("Signup Successful !!")
    return render(request, "website/signuppage.html")

def signup(request):
    return render(request, "website/signuppage.html")

def base(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'website/basepage.html')
        else:
            message = "Please try again"
            return render(request, "website/loginpage.html", {'login_page': message})
            
    return render(request, "website/loginpage.html")

def retrievedata(request):
    if request.method == "POST":
        city_name = request.POST["city"]
        aqi_data = cityairquality.objects.filter(city_name=city_name).first()
        return render(request, 'website/datapage.html', {'aqi_data': aqi_data})
    return render(request, 'website/basepage.html')

def home(request):
    return render(request, 'website/home.html')



@require_GET
def get_air_quality_news(request):
    api_key = 'your_api_key'
    url = f'https://newsapi.org/v2/everything?q=air%20quality%20OR%20climate%20OR%20weather%20OR%20pollution%20OR%20rain%20OR%20smoke%20OR%20temperature&sortBy=publishedAt&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Filter articles to only include those relevant to air quality, weather, pollution, etc.
        filtered_articles = []
        keywords = ['air quality', 'climate', 'weather', 'pollution', 'rain', 'smoke', 'temperature']
        
        for article in data['articles']:
            for keyword in keywords:
                if keyword in article['title'].lower() or keyword in article['description'].lower():
                    filtered_articles.append(article)
                    break  # Stop checking further keywords for this article
        
        # Create a response with filtered articles
        return JsonResponse({'status': 'ok', 'articles': filtered_articles})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


