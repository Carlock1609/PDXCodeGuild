from django.contrib import admin
from inboxApp.models import InboxDB, UserConversation

# Register your models here.
admin.site.register(InboxDB)
# admin.site.register(DirectMsgDB)
admin.site.register(UserConversation)