from django.shortcuts import render, redirect
from pages.models import UserImage
from user.models import CustomUser

# Create your views here.
def UploadPhoto(request):
    images = UserImage.objects.all()

    context = {
        'images': images,
    }
    return render(request, 'profile.html', context)

def upload_image(request):
    my_image = request.FILES['my_image']
    model = UserImage(CustomUser, my_image=my_image)
    model.save()


def new_image(request):
    if(request.method == 'POST'):
        # else posts task to list DB
        #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
        new_image = UserImage.objects.create(
            user_image = request.POST['user_image'],
        )
        new_image.save()
        # returns to list page
    elif(request.method == 'GET'):
            # sends user to create.html to add task
        return render(request, 'profile.html')

    return redirect('profile')