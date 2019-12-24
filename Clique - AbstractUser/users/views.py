from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Profile, CustomUser
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def home(request):
    return render(request, 'users/home.html')
