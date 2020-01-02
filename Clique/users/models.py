from django.db import models
# THIS IMPORTS BUILTIN USER MODEL
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # The param gives it a one to one relationship, models.CASCADE means if user is deleted, then everything is gone.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(default='', max_length=20)
    city = models.CharField(default='', max_length=30)
    socialname = models.CharField(max_length=30)
    bio = models.TextField(default='', max_length=500)
    followeramount = models.IntegerField(default=0,)
    portfolio = models.URLField(default='', max_length=100)
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# MUST INSTALL PILLOW



# class PostCreateView(CreateView): # This template only has two fields for the form.
#     model = Post  
#     fields = ['title', 'content']