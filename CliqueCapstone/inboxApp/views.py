from django.shortcuts import render
from .models import InboxDB, DirectMsgDB

# Create your views here.
def user_inbox(request):
    context = {
        'messages': InboxDB.objects.all(),
    }
    return render(request, 'inbox/user-inbox.html', context)

def direct_msg(request):
    context = {
        'messages': DirectMsgDB.objects.all(),
    }
    return render(request, 'inbox/direct-msg.html', context)