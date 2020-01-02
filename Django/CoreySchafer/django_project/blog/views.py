from django.shortcuts import render
from .models import Post

# makes you login before posting
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# LIST BASED VIEWS - 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class PostCreateView(LoginRequiredMixin, CreateView): # This template only has two fields for the form.
    model = Post  
    fields = ['title', 'content']

    # This sets the post form to have the current logged in user. OVERRIDE
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # This template only has two fields for the form.
    model = Post  
    fields = ['title', 'content']

    # This sets the post form to have the current logged in user. OVERRIDE
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # Checking to see if person making post is author logged in
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # Checking to see if person making post is author logged in
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})