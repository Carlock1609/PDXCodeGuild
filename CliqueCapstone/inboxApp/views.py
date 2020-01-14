from django.shortcuts import render
from .models import InboxDB
from users.models import CustomUser

from django.contrib.auth.decorators import login_required # Decorators

# MUST DO THIS VIEW TO GET THE ONES SENT TO YOU AND ONES YOUVE SENT
# Need to figure out security issue, user is able to type id number and get in without  login

# THIS IS WORKING
@login_required
def user_inbox(request):
    user_id = request.user.id
    if request.method == "GET":
        context = {
            'inbox_tos': InboxDB.objects.filter(sender=user_id),
            'inbox_froms': InboxDB.objects.filter(receiver=user_id), # I DONT NEED THIS, BECAUSE NAY POST DIRECTED TO ME SHOULD BE THE SAME
        }
        return render(request, 'inbox/user_inbox_list.html', context)

    elif request.method == "POST": # OTHER THINGS
        return render(request, 'inbox/user_inbox_list.html', context)

# WORK ON THIS
@login_required
def user_msg(request, id): # Use this view to continue the conversation
    user_id = request.user.id

    if request.method == "GET":
        context = {
            'inbox_tos': InboxDB.objects.order_by('sender','receiver','-sent_date').distinct('sender', 'receiver'),
            # 'inbox_froms': InboxDB.objects.filter(sender=id),
        }
        return render(request, 'inbox/user_inbox_msg.html', context)

# working one
# messages = InboxDB.objects.order_by('sender','receiver','-sent_date').distinct('sender', 'receiver')

# messages = Message.objects.order_by('fromUser','toUser','createdAt').distinct('fromUser', 'toUser')

# TESTING
# @login_required
# def user_inbox(request, id):
#     user1 = InboxDB.objects.all()
#     conv_id = user1[id].conversation.id

#     user1 = request.user.id

#     context = {
#         'inbox_msgs': InboxDB.objects.filter(user1=id),
#     }
#     return render(request, 'inbox/user_inbox_list.html', context)

# @login_required
# def user_msg(request, id):
#     return render(request, 'inbox/user_inbox_msg.html', {'inbox_msgs': InboxDB.objects.get(id=id)})
