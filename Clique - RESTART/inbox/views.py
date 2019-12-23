from django.shortcuts import render

# Create your views here.
def search_page(request):
    return render(request, 'inbox/search_page')

def community_page(request):
    return render(request, 'inbox/community_page')














# It looks like your view and the URL won't end up answering your question of getting all messages between A - B. At best, you could get all messages from A or all messages to B. Since you have the sender/receiver on the message, you could just change the view to:

# def getMessages(request, username):
#   user = User.objects.get(username=username)
#   messages = Messages.objects.filter(sender=user).order_by('-date')
#   return render(request, "inbox/chatBox.html", {'messages': messages})    
               

# BOTTOM ONE ERROR TOP CORRECT

# def getMessages(request, username):
#     user = User.objects.get(username=username)
#     # get the inbox related to the request.user and user
#     inbox = Inbox.objects.get('Whats will I write here');
#     messages = inbox.messages.all().order_by('-date')
#     return render(request, "inbox/chatBox.html", {'messages': messages})