from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from django.contrib.auth.decorators import login_required # Decorators
from django.contrib.auth import authenticate, login # More authentication
# from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms

from .models import CustomUser, UserProfile, ProfilePhotoLibrary
from .forms import CustomUserCreationForm, ProfileUpdateForm, ProfilePostForm

from django.contrib import messages
import boto3

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def profile_page(request):
    # user_id = request.user.id
    # profile = UserProfile.objects.get(user_id=user_id)
    
    # FIGURE OUT HOW TO DELETE PICTURE WHEN REPLACED
    # pic = profile.profile_picture
    # s3 = boto3.resource('s3')
    # obj = s3.Object('django-clique-files', 'pic')
    # obj.delete()

    if request.method == 'POST':
        # UserProfile.profile_picture # why are these here? Test this to see
        # UserProfile.cover_picture
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.user)
        user_id = request.user.id
        context = {
            'p_form': p_form,
            'user_profile': UserProfile.objects.get(user_id=user_id),
        }
        return render(request, 'users/profile.html', context)

# Consider making a new view and template to submit multiple photos
@login_required
def create_photo_post(request):
    if request.method == 'POST':
        # ProfilePhotoLibrary.photo_post
        l_form = ProfilePostForm(request.POST, request.FILES, instance=request.user.user)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'Your post has been created!')
            return redirect('profile')
    else:
        l_form = ProfilePostForm(request.POST, instance=request.user.user)
        user_id = request.user.id
        context = {
            'l_form': l_form,
            'user_profile': UserProfile.objects.get(user_id=user_id)
        }
        return render(request, 'users/profile.html', context)


# def edit_user(request, pk):
#     user = CustomUser.objects.get(pk=pk)
#     user_form = UserProfileForm(instance=user)
 
#     ProfileInlineFormset = inlineformset_factory(CustomUser, UserProfile, fields=('first_name', 'social_media', 'follower_amount', 'experience', 'portfolio_links', 'bio', 'city', 'country', 'friends',))
#     formset = ProfileInlineFormset(instance=user)
 
#     if request.user.is_authenticated() and request.user.id == user.id:
#         if request.method == "POST":
#             user_form = UserProfileForm(request.POST, request.FILES, instance=user)
#             formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
#             if user_form.is_valid():
#                 created_user = user_form.save(commit=False)
#                 formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
#                 if formset.is_valid():
#                     created_user.save()
#                     formset.save()
#                     return HttpResponseRedirect('/accounts/profile/')
 
#         return render(request, "account/account_update.html", {
#             "noodle": pk,
#             "noodle_form": user_form,
#             "formset": formset,
#         })
#     else:
#         raise PermissionDenied