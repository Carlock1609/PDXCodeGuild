from django.shortcuts import render, redirect
from users.models import UserProfile, CustomUser, ProfilePhotos
from django.contrib.auth.decorators import login_required # Decorators
from django.utils.decorators import method_decorator
# CUSTOM SEARCH
from django.db.models import Q

# STRIPE
from django.conf import settings
import stripe
from django.views.generic.base import TemplateView




def home(request):
    if request.user.is_authenticated:

        # MINOR FIX UNTIL SOLUTION FOUND
        # FIGURE OUT HOW TO CACHE
        images = ProfilePhotos.objects.order_by('?')[:1]

        context = {
            'images': images,
            'user_profile': UserProfile.objects.all()
        }
        return render(request, 'pages/home.html', context)
    else:
        return redirect('login')

def about(request):
    return render(request, 'pages/about.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'pages/donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Donations',
            source=request.POST['stripeToken'],
        )
        return render(request, 'pages/charge.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        follower = int(request.POST.get('follower_amount'))
        professions = request.POST.get('profession')

        if query == None and follower == None:
            return render(request, 'pages/search.html')
        else:

            if follower == 0:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), Q(follower_amount__gte=follower), Q(profession__icontains=professions))
            elif follower == 100:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), Q(follower_amount__lte=follower), Q(profession__icontains=professions))
            elif follower == 1000:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), (Q(follower_amount__lte=follower) & Q(follower_amount__gte=follower-900)), Q(profession__icontains=professions))
            elif follower == 5000:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), (Q(follower_amount__lte=follower) & Q(follower_amount__gte=follower-4000)), Q(profession__icontains=professions))
            elif follower == 10000:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), (Q(follower_amount__lte=follower) & Q(follower_amount__gte=follower-5000)), Q(profession__icontains=professions))
            elif follower == 50000:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), (Q(follower_amount__lte=follower) & Q(follower_amount__gte=follower-40000)), Q(profession__icontains=professions))
            elif follower == 100000:
                results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(location__icontains=query) | Q(user__username=query) | Q(user__username__istartswith=query), (Q(follower_amount__lte=follower) & Q(follower_amount__gte=follower-50000)), Q(profession__icontains=professions))
            
            context = {
                'results': results,
            }

            return render(request, 'pages/search.html', context)
    else:
        return render(request, 'pages/search.html')



# f request.method == 'POST':
#         # print(request.FILES)
#         image_file = request.FILES.get('image_file')
#         image_type = request.POST.get('image_type')

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
