from django.shortcuts import render
from .models import Post
# LIST BASED VIEWS - 
from django.views.generic import ListView, DetailView, CreateView
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
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # how to change posts. - makes it newest

class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView): # This template only has two fields for the form.
    model = Post  
    fields = ['title', 'content']

    # This sets the post form to have the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})