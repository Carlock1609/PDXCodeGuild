from django.db import models
from users.models import CustomUser    # FIGURE OUT WHY THIS CAUSES AN IMPORTING ERROR. 

import datetime
from django.db.models.signals import post_save

class InboxDB(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
    body = models.CharField(max_length=1000, default='', blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} TO {self.receiver} Messages"

# TEST THIS SIGN UP USER
# def create_inbox(sender, **kwargs):
#     if kwargs['created']:
#         user_inbox = InboxDB.objects.create(user=kwargs['instance'])
        
# post_save.connect(create_inbox, sender=CustomUser)