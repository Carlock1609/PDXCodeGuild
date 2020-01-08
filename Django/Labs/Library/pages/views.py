from django.shortcuts import render, redirect
from pages.models import UserImage
from user.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def UploadPhoto(request):
    if(request.method == 'POST'):
        
        UserImage.objects.create(
            user_image = request.FILES['user_image'],
        )
        return redirect('profile')


@login_required
def profile(request):
    images = UserImage.objects.all()

    context = {
        'images': images,
    }

    return render(request, 'profile.html', context)
