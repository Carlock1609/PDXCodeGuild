from django.shortcuts import render, redirect
from random_string import random_gen
from .models import URLS

# Create your views here.
def index(request):
    urls = URLS.objects.all()

    context = {
        'urls': urls,
    }
    return render(request, 'redirector/index.html', context)

def saveurl(request):
    if(request.method == 'GET'):
            # sends user to create.html to add task
        return render(request, 'redirector/saveurl.html')
    elif(request.method == 'POST'):
        # else posts task to list DB
        #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
        new_url = URLS.objects.create(
            url = request.POST['url'],
            code = random_gen(),
        )
        new_url.save()
        # returns to list page
        return redirect('index')


def redirecting(request, code):
    a_url = URLS.objects.get(code = code)
    context = {
        'a_url': a_url
    }

    return render(request, 'redirector/redirecting.html', context)
