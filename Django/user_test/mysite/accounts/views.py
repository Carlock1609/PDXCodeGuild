from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model()

def user_register(request):
    if request.method == 'POST':
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
        )
        new_user.set_password(request.POST['password']) # THIS IS A BUILTIN METHOD FROM THE USER OBJECT, MUST USE OUTSIDE FORM LIKE SO, IF IT WAS IN THE FORM IT WOULD JUST BE A STRING AND NOT A PASSWORD. THIS MAKES IT AN ACTUAL PASSWORD
        new_user.save()
        return redirect('login')
    return render(request, 'register/register.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
            )
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'register/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')