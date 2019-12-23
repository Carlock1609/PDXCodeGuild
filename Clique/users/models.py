from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    firstname = models.CharField(default='', max_length=20)
    city = models.CharField(default='', max_length=30)
    socialname = models.CharField(max_length=30)
    bio = models.TextField(default='', max_length=500)
    followeramount = models.IntegerField(default='', max_length=50)
    portfolio = models.URLField(default='', max_length=100)
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

