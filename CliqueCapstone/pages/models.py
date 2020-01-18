from django.db import models
from users.models import CustomUser, UserProfile
from inboxApp.models import InboxDB

from django.db.models.signals import post_save
from PIL import Image
import uuid # S3 bucket

import datetime
from django.utils import timezone

# Create your models here.

# ADD A ONETOONE FIELD TO THE model in Profile to get Profiles images to home images to randomly post
# class PhotoLibrary(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created_at = models.DateTimeField(autorunru_now_add=True)
#     title = models.CharField(max_length=100)
#     photo = models.ImageField(blank=True, null=True, upload_to=''


# profile_picture = models.ImageField(blank=True, null=True, upload_to='profile/profile_images/', editable=True) # FIGURE OUT PILLOW FROM LIBRARY LAB
# cover_picture = models.ImageField(blank=True, null=True, upload_to='profile/profile_backgrounds/', editable=True)