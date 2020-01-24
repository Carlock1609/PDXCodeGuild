from django.db import models
from users.models import CustomUser, UserProfile    # FIGURE OUT WHY THIS CAUSES AN IMPORTING ERROR. 

from django.db.models.signals import post_save
import datetime
from django.utils import timezone

# CREATE ANOTHER MODEL THAT HAS A UNIQUE THREAD ASSOCIATED WITH IT. VAN USES EQUIPMENT ID FROM HIS MODEL. YOU NEED TO MAKE A THREAD INBOX WITH ID FOR THE USERS TO POST TO

# class UserInbox(models.Model):
#     owner = models.ForeignKey(CustomUser, related_name='owner', on_delete=models.CASCADE, null=True)
    
#     class Meta:
#         verbose_name_plural = "User Inbox's"

#     def __str__(self):
#         return f"{self.owner}'s Inbox"
    

class UserMessages(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.CASCADE, null=True)
    conversation_name = models.CharField(max_length=200, default="User1 and User2's Conversation", null=True) # BE SURE TO MAKE THIS NONE EDITABLE AND FIGURE OUT WAY TO INSERT USERNAMES
    subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
    body = models.CharField(max_length=1000, default='', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user_inbox = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "User Individual Messages"

    def __str__(self):
        return f"{self.conversation_name}"


# >>> msg = UserMessages.objects.all()
# >>> msg
# <QuerySet [<UserMessages: Carlock906 sent a message to Carlock1609>, <UserMessages: Carlock1609 sent a message to Carlock906>]>
# >>> msg[0]
# <UserMessages: Carlock906 sent a message to Carlock1609>
# >>> msg[0].id
# 1
# >>> msg[0].user_inbox
# <UserProfile: Carlock1609's Profile>
# >>> msg[0].user_inbox.id
# 17
# >>> msg2 = UserMessages.objects.all()
# >>> msg2
# <QuerySet [<UserMessages: Carlock906 sent a message to Carlock1609>, <UserMessages: Carlock1609 sent a message to Carlock906>]>
# >>> msg2[1]
# <UserMessages: Carlock1609 sent a message to Carlock906>
# >>> msg2[1].id
# 2
# >>> msg2[1].user_inbox.id
# 17
# >>> msg2[1].sender
# <CustomUser: Carlock1609>
# >>> msg2[1].receiver
# <CustomUser: Carlock906>
# >>> msg2[0].sender
# <CustomUser: Carlock906>


# >>> user2 = UserProfile.objects.all()
# >>> user2
# <QuerySet [<UserProfile: testuser3's Profile>, <UserProfile: testuser1's Profile>, <UserProfile: testuser2's Profile>, <UserProfile: Carlock906's Profile>, <UserProfile: carlock9069's Profile>, <UserProfile: Carlock1609's Profile>]>
# >>> user2[4]
# <UserProfile: carlock9069's Profile>
# >>> user2[3]
# <UserProfile: Carlock906's Profile>
# >>> user2[3].id
# 13

# >>> from inboxApp.models import InboxDB
# >>> msg = InboxDB.objects.all()
# >>> msg
# <QuerySet [<InboxDB: Carlock1609 sent a message to Carlock906>]>
# >>> msg[0]
# <InboxDB: Carlock1609 sent a message to Carlock906>
# >>> msg[0].id
# 6
# >>> msg[0].profile_id
# <UserProfile: Carlock906's Profile>
# >>> msg[0].profile_id.id
# 13
# >>> user2 =

# >>> from users.models import ProfileUserPhoto
# >>> user1 = ProfileUserPhoto.objects.all()
# >>> user1
# <QuerySet [<ProfileUserPhoto: ProfileUserPhoto object (1)>, <ProfileUserPhoto: ProfileUserPhoto object (2)>, <ProfileUserPhoto: ProfileUserPhoto object (3)>, <ProfileUserPhoto: ProfileUserPhoto object (4)>, <ProfileUserPhoto: ProfileUserPhoto object (5)>, <ProfileUserPhoto: ProfileUserPhoto object (6)>, <ProfileUserPhoto: ProfileUserPhoto object (7)>, <ProfileUserPhoto: ProfileUserPhoto object (8)>, <ProfileUserPhoto: ProfileUserPhoto object (9)>, <ProfileUserPhoto: ProfileUserPhoto object (10)>, <ProfileUserPhoto: ProfileUserPhoto object (11)>, <ProfileUserPhoto: ProfileUserPhoto object (12)>, <ProfileUserPhoto: ProfileUserPhoto object (13)>]>
# >>> user1[0]
# <ProfileUserPhoto: ProfileUserPhoto object (1)>
# >>> user1[0].image
# <ImageFieldFile: User_photo_library/Three_bridge_brewing1.png>
# >>> user1[0].id
# 1
# >>> user1[13]
# >>> user1[12]
# <ProfileUserPhoto: ProfileUserPhoto object (13)>
# >>> user1[12].id
# 13
# >>> user1[12].user
# >>> user1[12].post
# <ProfileUserPost: ProfileUserPost object (5)>
# >>> user1[12].post.id
# 5

# >> user2 = ProfileUserPost.objects.get(id=5)
# >>> user2
# <ProfileUserPost: ProfileUserPost object (5)>
# >>> user2.id
# 5
# >>> user2.image
# >>> user2.title
# 'kjl'
# >>> user2 = ProfileUserPost.objects.all()
# >>> user2
# <QuerySet [<ProfileUserPost: ProfileUserPost object (1)>, <ProfileUserPost: ProfileUserPost object (2)>, <ProfileUserPost: ProfileUserPost object (3)>, <ProfileUserPost: ProfileUserPost object (4)>, <ProfileUserPost: ProfileUserPost object (5)>]>
# >>> user2[5]
# IndexError: list index out of range
# >>> user2[4]
# <ProfileUserPost: ProfileUserPost object (5)>
# >>> user2[4].id
# 5
# >>> user2[4].title
# 'kjl'
# >>> user2[4].user
# <CustomUser: Carlock1609>
# >>> user2[1]
# <ProfileUserPost: ProfileUserPost object (2)>
# >>> user2[1].user
# <CustomUser: Carlock906>
# >>> user2[0].user
# <CustomUser: Carlock906>
# >>> user2[2].user
# <CustomUser: carlock9069>




# class ConversationDB(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     conversation = models.ForeignKey(InboxDB, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "User Conversation"

#     def __str__(self):
#         return f"{self.user}"

    



# I NEED TO MAKE ANOTHER DB, ONE DB TO HAVE A PRIVATE INBOX ONETOONE WITH USER, AND THEN ANOTHER DB TO HAVE THE ID's ASSOCIATED TO THE USER AND SENDER

# HOWEVER, it only shows on one side

# WAIT A SECOND. BUT IF I HAVE ONE DB. AND I JUST FILTER THROUGH THEM, 
# HOWEVER, it only shows on one users side, so if a user receives a msg, it doesnt get the sent one.

# ON THE VIEWS I MAY HAVE FOUND SOLUTION, YOU MUST ADD TO THE CONTEXT AND LOOK FOR MATCHES OF receiver=id AND sender=id
# MUST DO THIS VIEW TO GET THE ONES SENT TO YOU AND ONES YOUVE SENT

# THIS IS THE WWORKING DB
# Find something to use Distinct with, Att = sender and receiver Conversation


# TESTING THIS MODEL SET
# class UserConversation(models.Model):
#     sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE, null=True)
#     receiver = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.CASCADE, null=True)
#     published = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "User Conversations"

#     def __str__(self):
#         if self.sender == self.sender:
#             return f"Message FROM {self.sender} TO {self.receiver}"
#         # THIS ISN'T WORKING CORRECTLY, IT PRINTS RIGHT BUT NOT THE FROM
#         elif self.receiver == self.receiver:
#             return f"Message TO {self.sender} FROM {self.receiver}"

# class InboxDB(models.Model):
#     # Able to query onetoone model
#     conversation = models.OneToOneField(UserConversation, related_name="conversation", on_delete=models.CASCADE, null=True, blank=True)
#     subject = models.CharField(max_length=100, default="Let's Collaborate!", blank=True, null=True)
#     body = models.CharField(max_length=1000, default='', blank=True, null=True)
#     sent_date = models.DateTimeField(auto_now_add=True)

    
#     class Meta:
#         verbose_name_plural = "User Inbox"
    
#     def __str__(self):
#         return f"{self.conversation.sender} and {self.conversation.receiver}"



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