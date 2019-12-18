from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# GET USERREGISTERFORM FROM FORM.py
# Create your views here.
def register(request):
    # Checks to see if method is POST
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # hashes password and secured.
            form.save()
            # is valid will have cleaned_data in dict
            username = form.cleaned_data.get('username')
            # flash message
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# DECORATED. USER MUST BE LOGGED IN TO GO INTO THIS PAGE -- from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    return render(request, 'users/profile.html')



# MESSAGES METHODS
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error