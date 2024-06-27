from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'signup'



        

class cityairquality(models.Model):
    city_name = models.CharField(max_length=100)
    air_quality = models.CharField(max_length=100)
    air_quality_index = models.IntegerField()
    
    class Meta:
        db_table = 'cityairquality'


