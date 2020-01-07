from django.shortcuts import render

# Create your views here.
# from .models import Post

posts = [
     {
         'author': 'CoreyMS',
         'title': 'Blog Post 1',
         'content': 'First post content',
         'date_posted': 'Augest 27, 2018',
     },
     {
         'author': 'Jane Doe',
         'title': 'Blog Post 2',
         'content': 'Second post content',
         'date_posted': 'Augest 28, 2018',
     }
 ]
def home(request):
        # DUMMY DATA - SWITCHING OUT TO MODEL DATA
    context = {
        'posts': posts
    }
    return render(request, "pages/home.html", context)

def welcome(request):
    return render(request, 'pages/welcome.html', {'title': 'Welcome'})