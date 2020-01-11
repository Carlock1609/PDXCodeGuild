from django.shortcuts import render
from .models import InboxDB, DirectMsgDB
from django.contrib.auth.decorators import login_required # Decorators

# Create your views here.
@login_required
def user_inbox(request, id):
    context = {
        'inbox': InboxDB.objects.get(users_inbox=id),
    }
    return render(request, 'inbox/user_inbox.html', context)

@login_required
def direct_msg(request, id):
    context = {
        'messages': DirectMsgDB.objects.get(sender=id),
    }
    return render(request, 'inbox/direct_msg.html', context)


