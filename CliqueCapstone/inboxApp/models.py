from django.db import models
from users.models import CustomUser
import datetime

# Create your models here.
class InboxDB(models.Model):
    messages = models.CharField(max_length=50, default='', blank=True, null=True)
    subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.user.username}'s Inbox"

class DirectMsgDB(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE)
    reciever = models.ForeignKey(CustomUser, related_name='reciever', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
    body = models.CharField(max_length=1000, default='', blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.user.username} - {self.user.username} Messages"

