from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from django.utils import timezone

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
    email = models.EmailField(default='', blank=True, null=True)

    social_media = models.URLField(default="") # FIGURE OUT HOW TO MAKE THIS REQUIRED THE FIRST TIME
    portfolio_links = models.URLField(blank=True, null=True) 

    follower_amount = models.IntegerField(blank=True, null=True) # USE THE API DATA TO STORE HERE, OTHERWISE USER MANUALLY ENTTERS IN AMOUNT

    bio = models.TextField(max_length=500, blank=True, null=True)
    # experience = models.TextField(max_length=500, blank=True, null=True) # CONSIDER DELETEING THIS

    location = models.CharField(max_length=80, blank=True, null=True)
    # city = models.CharField(max_length=20)
    # state = models.CharField(max_length=3)

    profile_picture = models.ImageField(default='../../static_images/default_profile.jpg', upload_to='profile/profile_images/', editable=True, blank=True, null=True) # FIGURE OUT PILLOW FROM LIBRARY LAB
    cover_picture = models.ImageField(default='static_images/default_bg.jpg', upload_to='profile/profile_backgrounds/', editable=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


    # Saves space and loading time
    # TRY AND ADD THE BG PHOTO TO THIS ASWELL
    def save_profile(self, *args, **kwargs): # ADDED TAGS FOR S3 BUCKETS
        super().save_profile(*args, **kwargs)

        profile_img = Image.open(self.profile_picture)

        if profile_img.height > 300 or profile_img.width > 300:
            output_size = (300, 300)
            profile_img.thumbnail(output_size)
            profile_img.save(self.profile_picture)

    # cover photo
    # This isnt reesizing too great - Get exact pixels
    def save_cover(self, *args, **kwargs):
        super().save_cover(*args, **kwargs)

        background_img = Image.open(self.cover_picture)

        if background_img.height > 100 or background_img.width > 400:
            output_size = (100, 400)
            background_img.thumbnail(output_size)
            background_img.save(self.cover_picture)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=CustomUser)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(CustomUser, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(CustomUser, related_name='from_user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_user.username}'s Friend {self.to_user.username}"



class ProfilePhotos(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    file = models.FileField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "UserProfile Photos"

    def __str__(self):
        return f"{self.file}"

    

class ProfileLibrary(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    file = models.FileField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Library Photos"

    def __str__(self):
        return f"{self.file}"

# class UserFriendsList(models.Model):
#     user = models.OneToOneField(CustomUser, related_name='users_friend_list', on_delete=models.CASCADE)
#     friends_list = models.ManyToManyField(CustomUser, related_name='friends_list')

#     class Meta:
#         verbose_name_plural = "FriendsList"

#     def __str__(self):
#         return f"{self.friends_list}"

# This will be photos for the user
# class ProfilePhotoLibrary(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.CharField(max_length=100, blank=True, null=True)
#     photo_post = models.ImageField(upload_to='profile/profile_library', editable=True, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username}'s Photo"

# CREATE CLASS FOR POSTS AND IMAGES

# # User post
# class ProfileUserPost(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
#     title = models.CharField(max_length=128, default="", blank=True, null=True)

# # User image 
# # Onetoone with ProfileUserPost
# class ProfileUserPhoto(models.Model):
#     post = models.ForeignKey(ProfileUserPost, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='User_photo_library', editable=True, blank=True, null=True)


