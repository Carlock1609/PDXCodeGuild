from django.db import models
from users.models import CustomUser    # FIGURE OUT WHY THIS CAUSES AN IMPORTING ERROR. 

import datetime
from django.db.models.signals import post_save

# I NEED TO MAKE ANOTHER DB, ONE DB TO HAVE A PRIVATE INBOX ONETOONE WITH USER, AND THEN ANOTHER DB TO HAVE THE ID's ASSOCIATED TO THE USER AND SENDER

# HOWEVER, it only shows on one side

# WAIT A SECOND. BUT IF I HAVE ONE DB. AND I JUST FILTER THROUGH THEM, 
# HOWEVER, it only shows on one users side, so if a user receives a msg, it doesnt get the sent one.

# ON THE VIEWS I MAY HAVE FOUND SOLUTION, YOU MUST ADD TO THE CONTEXT AND LOOK FOR MATCHES OF receiver=id AND sender=id
# MUST DO THIS VIEW TO GET THE ONES SENT TO YOU AND ONES YOUVE SENT

class InboxDB(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
    body = models.CharField(max_length=1000, default='', blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inboxes"

    def __str__(self):
        if self.sender == self.sender:
            return f"Message from {self.sender} TO {self.receiver}"
        elif self.receiver == self.receiver:
            return f"Message to {self.sender} FROM {self.receiver}"

# class UserConversation(models.Model):
#     body = models.CharField(max_length=1000)
#     date_sent = models.DateTimeField(auto_now_add=True)


    # # security mixins, add to all models?
    # def test_func(self):
    #     msg = self.get_object()
    #     if self.request.user == msg.author:
    #         return True
    #     return False

# class UserMessages(models.Model):
#     user_messages = models.ForeignKey(InboxDB, related_name='users_inbox', on_delete=models.CASCADE, null=True)


# WOKRING ON THIS
# class InboxDB(models.Model):
#     sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE, null=True)
#     receiver = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.CASCADE, null=True)
#     subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
#     # body = models.CharField(max_length=1000, default='', blank=True, null=True)
#     # published = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Inboxes"

#     def __str__(self):
#         return f"{self.receiver} Conversation: {self.subject}"

# class UserConversation(models.Model):
#     body = models.CharField(max_length=1000)
#     date_sent = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.receiver}"