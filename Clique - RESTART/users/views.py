from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'users/login.html')

def logout_page(request):
    return render(request, 'users/logout.html')

def register_page(request):
    return render(request, 'users/register.html')

def profile_page(request):
    return render(request, 'users/profile.html')