from django.shortcuts import render, redirect
from users.models import UserProfile, CustomUser, ProfilePhotos
from django.contrib.auth.decorators import login_required # Decorators
from django.utils.decorators import method_decorator
from django.db.models import Q
# search filters
# from django.contrib.postgres.search import SearchVector



# Create your views here.

def home(request):
    if request.user.is_authenticated:

        images = ProfilePhotos.objects.order_by('?')

        context = {
            'images': images,
            'user_profile': UserProfile.objects.all()
        }
        return render(request, 'pages/home.html', context)
    else:
        return redirect('login')

def about(request):
    return render(request, 'pages/about.html')

# ADD USERNAME TO SEARCH
def search(request):
    query = request.GET.get('q')
    if query == None:
        return render(request, 'pages/search.html')
    else:
        # THIS WORKS BUT FIGURE OUT HOW THE FLOW WOULD WORK
        # Q(follower_amount__gte=query) AND Q(follower_amount__lte=query)
        results = UserProfile.objects.filter(Q(follower_amount__icontains=query) | Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__startswith=query))
        context = {
            'results': results,
        }

        return render(request, 'pages/search.html', context)


# if request.method == 'GET':
#     context = {
#         'user_filter': UserProfile.objects.filter(city=city),
#     }
#     return render(request, 'pages/search.html', context)

    

# class SearchView(ListView):
#     model = UserProfile
#     template_name = 'pages/search.html'
#     context_object_name = 'all_search_results'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_name = self.request.GET.get('search', '')
#         context['all_search_results'] = CustomUser.objects.filter(username__icontains=user_name)
#         return context

# def newsearch(request):
#     search_query = 'name'
#     UserProfile.objects.filter(first_name__unaccent__startswith=search_query)
