from django.shortcuts import render
from users.models import UserProfile, CustomUser

# Create your views here.
def home(request):
    return render(request, 'pages/home.html', {'user_profile': UserProfile.objects.all()})

def about(request):
    return render(request, 'pages/about.html')