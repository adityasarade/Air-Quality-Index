# Air Quality Index

## Introduction
The Air Quality Index (AQI) is a web application that provides users with real-time air quality information for their specific areas. Users can sign up, log in, and access air quality data. The homepage displays the latest news about air quality, and after logging in, users can view detailed AQI data for their city or selected areas.

## Features
- **User Authentication**: Users can sign up and log in.
- **Homepage**: Displays the latest news on air quality.
- **AQI Data**: After logging in, users can access air quality data for their city or specified areas.
- **API Integration**: Fetches real-time air quality data using an external API.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: MySQL
- **API**: Air Quality news API for fetching real-time data

## How to Use

### Steps
1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/aqi-management-system.git
    ```
    ```bash
    cd aqi-management-system
   ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Set up your MYSQL Database**
   ```bash
   CREATE DATABASE AQI
   ```
   
4. **Connect Django to MYSQL**
    ```bash
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'AQI',
              'USER': 'your_mysql_username',
              'PASSWORD': 'your_mysql_password',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
    ```

5. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6. **Start the development server**
    ```bash
    python manage.py runserver
    ```

7. **Navigate in your web browser**
   ```bash
   http://127.0.0.1:8000/
   ```

## API Key Configuration
To fetch real-time air quality data, you need to configure your API key:

1. **Obtain an API key** from an air quality data provider.
2. **Set the API key** in your Django apps/views.py file. 
