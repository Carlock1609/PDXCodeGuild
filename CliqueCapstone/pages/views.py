from django.shortcuts import render
from users.models import UserProfile, CustomUser

# Create your views here.
def home(request):
    context = {
        'user': CustomUser.objects.all(),
        'user_profile': UserProfile.objects.all(),
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')