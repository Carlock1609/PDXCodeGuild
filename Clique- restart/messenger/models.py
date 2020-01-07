from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

# Should I create this one to many? One User has access to many emails from other users?
# class InboxDB(models.Model):
#     to = models.CharField(max_length=100,)
#     subject = models.CharField(max_length=200, blank=True, Null=True,)
#     body = models.TextField(max_length=3000,)
#     sent = models.DateTimeField(auto_now_add=True,)
#     sender = models.ForeignKey(
#                     User,
#                     unique=True,
#                     on_delete=models.CASCADE,
#                     null=True,
#                     blank=True, 
#                     related_name="sender",
#                     )
#     receiver = models.ForeignKey(
#                     User,
#                     unique=True,
#                     on_delete=models.CASCADE,
#                     null=True,
#                     blank=True,
#                     related_name="receiver",
#                     )    

#     def __str__(self):
#         return f'{self.InboxDB.to}'
