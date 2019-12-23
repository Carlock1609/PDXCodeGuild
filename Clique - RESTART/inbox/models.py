from django.db import models

# Create your models here.


















# class Inbox(models.Model):
#       by_user = models.ForeignKey(User); # who starts messaging
#       to_user = models.ForeignKey(User); # second user

# class Message(models.Model):
#       sender = models.ForeignKey(User); # who starts messaging
#       receiver = models.ForeignKey(User); # second user
#       inbox = models.ForeignKey(Inbox); # message belongs to the inbox


# ORR



# class Message(models.Model): 
#     subject = models.TextField(max_length=1000, blank=True)
#     text = models.TextField(max_length=10000, blank=True)
#     sender = models.ForeignKey(
#                     settings.AUTH_USER_MODEL,
#                     on_delete=models.CASCADE,
#                     null = True, 
#                     related_name="sender"
#                     )
#     receiver = models.ForeignKey(
#                     settings.AUTH_USER_MODEL,
#                     on_delete=models.CASCADE,
#                     null = True, 
#                     related_name="receiver"
#                     )    