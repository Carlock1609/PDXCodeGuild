from django.shortcuts import render
from .models import InboxDB
from users.models import CustomUser

from django.contrib.auth.decorators import login_required # Decorators
from django.contrib.auth.decorators import user_passes_test # CREATE TEST FOR WHEN YOU WANT TO ADD SECURITY

# MUST DO THIS VIEW TO GET THE ONES SENT TO YOU AND ONES YOUVE SENT
# Need to figure out security issue, user is able to type id number and get in without  login

# RESEARCH DISTINCT AND VALUES AND ORDERBY

@login_required
def user_inbox(request):
    user_id = request.user.id
    if request.method == "GET":

        message_sender = InboxDB.objects.filter(sender=user_id)
        message_receiver = InboxDB.objects.filter(receiver=user_id)
        
        context = {
            'message': message_sender.order_by('subject', '-sent_date').distinct('subject'),
            'message': message_receiver.order_by('subject', '-sent_date').distinct('subject'),
        }
        return render(request, 'inbox/user_inbox_list.html', context)

    elif request.method == "POST": # CREATE POST FORM
        return render(request, 'inbox/user_inbox_list.html', context)

# WORK ON TEMPLATE
@login_required
def user_msg(request): # Use this view to continue the conversation
    user_id = request.user.id

    # if request.CustomUser.username == message.sender.username

    if request.method == "GET":
        
        context = {
            'message': InboxDB.objects.filter(sender=user_id).order_by('subject', '-sent_date').distinct('subject'),
            'message': InboxDB.objects.filter(receiver=user_id).order_by('subject', '-sent_date').distinct('subject'),
        }
        return render(request, 'inbox/user_inbox_msg.html', context)

    elif request.method == "POST": # CREATE POST FORM
        return render(request, 'inbox/user_inbox_msg.html', context)

 # SUBJECT DISTINCT
# >>> message_sender = InboxDB.objects.filter(sender=1)
# >>> message_sender.order_by('subject', '-sent_date').distinct('subject')
# <QuerySet [<InboxDB: Carlock906 and testuser1's Conversation>, <InboxDB: Carlock906 and testuser2's Conversation>]>
# >>> message_receiver = InboxDB.objects.filter(receiver=1)
# >>> message_receiver.order_by('subject', '-sent_date').distinct('subject')
# <QuerySet [<InboxDB: testuser1 and Carlock906's Conversation>]>


# ID's DISTINCT
# >>> message_sender.order_by('sender', 'receiver', '-sent_date').distinct('sender', 'receiver')
# <QuerySet [<InboxDB: Carlock906 and testuser1's Conversation>, <InboxDB: Carlock906 and testuser2's Conversation>]>
# >>> message_receiver = InboxDB.objects.filter(receiver=1)
# >>> message_receiver.order_by('receiver', 'sender', '-sent_date').distinct('receiver', 'sender')
# <QuerySet [<InboxDB: testuser1 and Carlock906's Conversation>]>
# >>>

# django.core.exceptions.FieldError: Invalid order_by arguments: ['receiver-sent_date']
# >>> message_sender.order_by('sender', 'receiver', '-sent_date').distinct('sender', 'receiver')
# <QuerySet [<InboxDB: Carlock906 and testuser1's Conversation>, <InboxDB: Carlock906 and testuser2's Conversation>]>
# >>> message_sender.order_by('sender', 'receiver', '-sent_date').distinct('sender', 'receiver')
# <QuerySet [<InboxDB: Carlock906 and testuser1's Conversation>, <InboxDB: Carlock906 and testuser2's Conversation>]>
# >>>

# working on distinct
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

