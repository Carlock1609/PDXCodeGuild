from django.shortcuts import render, redirect
from users.models import UserProfile, CustomUser

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html', {'user_profile': UserProfile.objects.all()})
    else:
        return redirect('login')

def about(request):
    return render(request, 'pages/about.html')