from django.shortcuts import render, redirect
from users.models import UserProfile, CustomUser
# search filters
# from django.contrib.postgres.search import SearchVector

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
    # user_filter = UserFilter(request.GET, queryset=user_list)
    context = {
        'user_list': UserProfile.objects.all()
    }
    return render(request, 'search/user_list.html', context)

class SearchView(ListView):
    model = UserProfile
    template_name = 'pages/search.html'
    context_object_name = 'all_search_results'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get('search', '')
        context['all_search_results'] = CustomUser.objects.filter(username__icontains=username)
        return context

# def newsearch(request):
#     search_query = 'name'
#     UserProfile.objects.filter(first_name__unaccent__startswith=search_query)