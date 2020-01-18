from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

import uuid # S3 bucket


# creating inbox instance when created aswell
# FIGURE OUT WHY THIS CAUSES AN IMPORTING ERROR. 
# from inboxApp.models import InboxDB

# Create your models here.
class CustomUser(AbstractUser):
    pass
# ADD ADDITIONAL FIELDS HERE

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20) # REQUIRED

    social_media = models.URLField(default="") # DEFAULT REQUIRED = ADD AUTH HERE
    portfolio_links = models.URLField(blank=True, null=True) 

    follower_amount = models.IntegerField(blank=True, null=True) # USE THE API DATA TO STORE HERE, OTHERWISE USER MANUALLY ENTTERS IN AMOUNT
    cliques = models.IntegerField(blank=True, null=True) # CALL IT CLIQUES # USER CANNOT FILL THIS IN 

    bio = models.TextField(max_length=500, blank=True, null=True)
    experience = models.TextField(max_length=500, blank=True, null=True)

    city = models.CharField(max_length=20)
    state = models.CharField(max_length=3)

    profile_picture = models.ImageField(default='default_profile.jpg', upload_to='profile/profile_images/', editable=True) # FIGURE OUT PILLOW FROM LIBRARY LAB
    cover_picture = models.ImageField(default='default_bg.jpg', upload_to='profile/profile_backgrounds/', editable=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # Saves space and loading time
    # TRY AND ADD THE BG PHOTO TO THIS ASWELL
    def save(self, *args, **kwargs): # ADDED TAGS FOR S3 BUCKETS
        super().save(*args, **kwargs)

        profile_img = Image.open(self.profile_picture)
        background_img = Image.open(self.cover_picture)

        if profile_img.height > 300 or img.width > 300:
            output_size = (300, 300)
            profile_img.thumbnail(output_size)
            profile_img.save(self.profile_picture)

        if background_img.height > 400 or img.width > 800:
            output_size = (400, 800)
            background_img.thumbnail(output_size)
            background_img.save(self.cover_picture)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=CustomUser)


class PhotoLibrary(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    photo = models.FileField()
