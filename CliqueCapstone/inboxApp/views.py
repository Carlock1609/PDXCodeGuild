from django.shortcuts import render, HttpResponse, redirect
from .models import UserMessages
from users.models import CustomUser, UserProfile

from django.contrib.auth.decorators import login_required # Decorators
from django.contrib import messages



@login_required
def user_inbox(request):
    user_id = request.user.id

    if request.method == "GET":
        context = {
            # SWAPPING THESE WILL MAKE IT NOT VISIBLE TO SENDER BUT VISIBLE TO RECIEVER AND VICE VERSA
            'message_list': UserMessages.objects.filter(sender=user_id).order_by('conversation_name', '-created_date').distinct('conversation_name'),
            'message_list': UserMessages.objects.filter(receiver=user_id).order_by('conversation_name', '-created_date').distinct('conversation_name'),
        }
        return render(request, 'inbox/user_inbox_list.html', context)

@login_required
def user_msg(request, id, conversation_name):
    # ID IS INDIVIDUAL MESSAGE ID, NOT USER ID
    user_id = request.user.id
    conversation = conversation_name

    # YASSS THIS WORKED.
    if request.method == 'POST':
        if request.user == UserMessages.objects.get(id=id).sender:
            receiver_id = UserMessages.objects.get(id=id).receiver.id
        else:
            receiver_id = UserMessages.objects.get(id=id).sender.id

        new_msg = UserMessages.objects.create(
            sender = CustomUser.objects.get(id=user_id),
            receiver = CustomUser.objects.get(id=receiver_id),
            conversation_name = conversation,
            body = request.POST['body'],
            user_inbox = UserMessages.objects.filter(conversation_name=conversation_name)[0].user_inbox,
        )
        new_msg.save()

        return redirect(f'/inbox/message/{id}/{conversation_name}/')

    if request.method == "GET":
        context = {
            'message': UserMessages.objects.filter(sender=user_id).order_by('sender', 'created_date'),
            'message': UserMessages.objects.filter(receiver=user_id).order_by('receiver', 'created_date'),
            'message': UserMessages.objects.filter(user_inbox=UserMessages.objects.get(id=id).user_inbox).order_by('user_inbox', 'created_date'),
            'message': UserMessages.objects.filter(conversation_name=conversation_name).order_by('conversation_name', 'created_date'),
        }
        return render(request, 'inbox/user_inbox_msg.html', context)


# Function based form letss go boysss
@login_required
def create_msg(request, id):
    user_id = request.user.id
    user_profile = CustomUser.objects.get(id=UserProfile.objects.get(id=id).user.id).id
    user1 = CustomUser.objects.get(id=user_id).username
    user2 = CustomUser.objects.get(id=UserProfile.objects.get(id=id).user.id).username

    if request.method == 'POST':
        new_msg = UserMessages.objects.create(
            sender = CustomUser.objects.get(id=user_id),
            receiver = CustomUser.objects.get(id=UserProfile.objects.get(id=id).user.id),
            conversation_name = f"{user1} and {user2}'s Conversation",
            subject = request.POST['subject'],
            body = request.POST['body'],
            user_inbox = UserProfile.objects.get(id=id),
        )

        new_msg_id = UserMessages.objects.get(id=new_msg.id).id


        new_msg.save()
        # FIGURE THIS BUG OUT, IF NOT REDIRECT TO LIST AND FIGURE OUT BETTER SOLUTION
        # return redirect(f'inbox/message/{new_msg_id}/{new_msg.conversation_name}/')
        return redirect(f'/users/profile/{user_profile}/')

    elif request.method =='GET':
        context = {
            'profile': UserProfile.objects.get(user=user_id),
            'sending_to': UserProfile.objects.get(id=id).user.username,
            'redirect': UserProfile.objects.get(id=id).user.id,
        }
        return render(request, 'inbox/user_inbox_create.html', context)



# >>> user2 = UserProfile.objects.get(id=17)
# >>> user2
# <UserProfile: Carlock1609's Profile>
# >>> user2.id
# 17

# <UserMessages: Carlock1609 and carlock9069's Conversation>
# >>> user[0].user_inbox
# <UserProfile: carlock9069's Profile>
# >>> user[0].user_inbox.id
# 18
# >>> user1 = UserMessages.objects.filter(user_inbox_id=18)
# >>> user1

# Class based
# @login_required
# def create_msg(request, id):
#     if request.method == 'POST':
#             # UserProfile.profile_picture # why are these here? Test this to see
#         # UserProfile.cover_picture
#         m_form = SendUserMessageForm(request.POST, instance=request.user.user)
#         if m_form.is_valid():
#             m_form.save()
#             messages.success(request, f'Message has been sent!')
#             return redirect('user-inbox')
#     else:
#         m_form = SendUserMessageForm(request.POST, instance=request.user.user)
#         context = {
#             'm_form': m_form,
#         }
#         return render(request, 'inbox/user_inbox_create.html', context)

# def add_todo(request):
#     if(request.method == 'GET'):
#         # sends user to create.html to add task
#         return render(request, 'todos/create.html')
#     elif(request.method == 'POST'):
#         # else posts task to list DB
#         #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
#         new_todo = Todo.objects.create(
#             title = request.POST['title'],
#             text = request.POST['text'],
#             status = request.POST['status'],
#             # user = request.user # MUST ADD IF YOU WANT TO HAD LIST FOR
#         )
#         new_todo.save()
#         # returns to list page
#     return redirect('list')



# view add a todo to the database. this view handles both GET and POST HTTP requests
# def add_todo(request):
#     if request.method == 'GET': # if its a GET request, just display the todos/add.html template
#         return render(request, 'todos/add.html')
#     elif request.method == 'POST': # if it's a POST request ...
#         title = request.POST['title']   # get the title from the POST submission, this comes form a form
#         text = request.POST['text']     # get the text from the POST submission, this comes form a form
#         if (request.POST['status'] == 'False'): # check the status because it's a string and booleans are not strings
#             status = False
#         else:
#             status = True
#         # add the new todo to the databse. objects.create() automatically saves the new todo for us so we
#         # don't need a separate call to the save() method
#         todo = Todo.objects.create(title = title, text = text, status = status)
#         return redirect('list')
#  FORM EXAMPLE
# <form action="{% url 'add' %}" method="POST">
#     {% csrf_token %}
#     title: <br> <input type="text" name="title" placeholder="enter todo title"><br>
#     description:<br> <textarea name="text" id="" cols="30" rows="10">type todo description here</textarea><br>
#     status: <br> <select name="status"><br>
#         <option value="True">True</option>
#         <option value="False">False</option>
#       </select> 
#       <br>
#     <input type="submit" value="add">
# </form>





# >>> user2 = UserProfile.objects.get(user=CustomUser.objects.get(username='Carlock1609'))
# >>> user2
# <UserProfile: Carlock1609's Profile>
# >>> user2.id
# 17

# FIGURING OUT HOW TO GRAB USERS PROFILE
# ***********
# >>> user1 = UserProfile.objects.get(user=CustomUser.objects.get(username='Carlock906'))
# >>> user1
# <UserProfile: Carlock906's Profile>
# *************


# >>> user1 = UserMessages.objects.filter(user_inbox=17)
# >>> user1
# <QuerySet [<UserMessages: Carlock906 sent a message to Carlock1609>, <UserMessages: Carlock1609 sent a message to Carlock906>]>

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

