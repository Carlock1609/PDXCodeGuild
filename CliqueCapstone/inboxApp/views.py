from django.shortcuts import render
from .models import InboxDB
from users.models import CustomUser

from django.contrib.auth.decorators import login_required # Decorators

@login_required
def user_inbox(request, id):
    return render(request, 'inbox/user_inbox_list.html', {'inbox_msgs': InboxDB.objects.filter(sender=id)})

@login_required
def user_msg(request, id):
    return render(request, 'inbox/user_inbox_msg.html', {'inbox_msgs': InboxDB.objects.get(id=id)})
