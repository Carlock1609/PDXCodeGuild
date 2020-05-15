from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

from catalog.models import BookInstance
User = get_user_model()

def login_user(request):
  if request.method == 'POST':
    user = authenticate(
      request,
      username = request.POST['username'],
      password = request.POST['password']
    )

    if user is not None:
      login(request, user)
      return redirect('dashboard')
    else:
      return render(request, 'accounts/login.html')
  else:
    return render(request, 'accounts/login.html')

def logout_user(request):
  logout(request)
  return redirect('index')

def register(request):
  if request.method == 'POST':
    data = request.POST
    print(data)
    user_exists = User.objects.filter(username = data['username']).exists()
    
    if data['password'] == data['password2'] and not user_exists:
      new_user = User(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        username = data['username'],
      )
      new_user.set_password(data['password'])
      new_user.save()
      return redirect('login')
    else:
      return render(request, 'accounts/register.html')
  else:
    return render(request, 'accounts/register.html')

def dashboard(request):
  user_books = BookInstance.objects.filter(borrower = request.user)
  context = {
    'user_books': user_books,
  }
  return render(request, 'accounts/dashboard.html', context = context)
