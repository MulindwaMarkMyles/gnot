from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    username = models.CharField(default="user")
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField()
    
    