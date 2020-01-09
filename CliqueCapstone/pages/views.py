from django.shortcuts import render
from users.models import UserProfile

# Create your views here.
def home(request):
    user_profile = UserProfile.objects.all()

    context = {
        'user_profile': user_profile
    }
    return render(request, 'pages/home.html', context)