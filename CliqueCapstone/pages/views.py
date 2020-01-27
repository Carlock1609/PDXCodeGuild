from django.shortcuts import render, redirect
from users.models import UserProfile, CustomUser

# filters
from .filters import UserFilter
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html', {'user_profile': UserProfile.objects.all()})
    else:
        return redirect('login')

def about(request):
    return render(request, 'pages/about.html')

def search(request):
    user_list = UserProfile.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})

class SnippetListView(ListView):
    model = UserProfile
    template_name = 'pages/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context
