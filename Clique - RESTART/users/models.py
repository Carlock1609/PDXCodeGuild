from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username



class Profile(models.Model):
    # The param gives it a one to one relationship, models.CASCADE means if user is deleted, then everything is gone.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user profile pic
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

INSTALL PILLOW