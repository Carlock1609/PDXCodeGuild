from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from .models import Profile, CustomUser

# when user is made send this signal and its received by receiver dec, 
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()