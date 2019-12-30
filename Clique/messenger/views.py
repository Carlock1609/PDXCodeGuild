from django.shortcuts import render

# Create your views here.
def inbox(request):
    return render(request, 'messenger/inbox.html')

def community(request):
    return render(request, 'messenger/inbox.html')