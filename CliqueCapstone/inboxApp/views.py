from django.shortcuts import render
from .models import InboxDB
from users.models import CustomUser

from django.contrib.auth.decorators import login_required # Decorators

# MUST DO THIS VIEW TO GET THE ONES SENT TO YOU AND ONES YOUVE SENT
# Need to figure out security issue, user is able to type id number and get in without  login

@login_required
def user_inbox(request, id):
    context = {
        'inbox_msgs': InboxDB.objects.filter(sender=id),
        'inbox_froms': InboxDB.objects.filter(receiver=id),
    }
    return render(request, 'inbox/user_inbox_list.html', context)

@login_required
def user_msg(request, id):
    return render(request, 'inbox/user_inbox_msg.html', {'inbox_msgs': InboxDB.objects.get(id=id)})
