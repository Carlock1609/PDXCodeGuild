from django.shortcuts import render
from .models import Post
# DUMMY DATA
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'Augest 27, 2018',
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'Augest 28, 2018',
#     }
# ]

# Create your views here.
def home(request):
    # DUMMY DATA - SWITCHING OUT TO MODEL DATA
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})