from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    username = models.CharField(default="user")
    surname = models.CharField(max_length=100)
    password = models.CharField()
    
    