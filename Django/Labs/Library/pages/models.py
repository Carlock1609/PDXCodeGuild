from django.db import models
from user.models import CustomUser

# Create your models here.

class UserImage(models.Model):
    user_image = models.ImageField(upload_to='images/')
    