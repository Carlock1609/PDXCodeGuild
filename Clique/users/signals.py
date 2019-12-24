from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when user is made send this signal and its received by receiver dec, 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# saves 
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
   instance.profile.save()

   # when finished here go to apps.py