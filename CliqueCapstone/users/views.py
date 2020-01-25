from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from django.contrib.auth.decorators import login_required # Decorators
from django.contrib.auth import authenticate, login # More authentication
# from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms

from .models import CustomUser, UserProfile, ProfileUserPost, ProfileUserPhoto
from allauth.socialaccount.models import SocialAccount
from .forms import CustomUserCreationForm, ProfileUpdateForm, PostForm, PhotoForm
from django.forms import modelformset_factory

from django.contrib import messages
import boto3

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
@login_required
def profile_page(request, id):


    # Multiple Photo posts
    ImageFormSet = modelformset_factory(ProfileUserPhoto, form=PhotoForm, extra=3)

    if request.method == 'POST':
        # ProfilePhotoLibrary.photo_post

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProfileUserPhoto.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = ProfileUserPhoto(post=post_form, image=image)
                    photo.save()
            messages.success(request, "Yeeew, check it out on the home page!")
            return redirect('profile')
        else:
            print(postForm.errors, formset.errors)

    else:
        postForm = PostForm()
        # Research queryset
        formset = ImageFormSet(queryset=ProfileUserPhoto.objects.none())
        # user_id = request.user.id
        create_msg = UserProfile.objects.get(user=CustomUser.objects.get(id=id))

        context = {
            'create_msg': create_msg,
            'auth': CustomUser.objects.get(id=id),
            'postForm': postForm,
            'formset': formset,
            'user_profile': UserProfile.objects.get(id=UserProfile.objects.get(user=CustomUser.objects.get(id=id)).id),
            'library': ProfileUserPhoto.objects.get(id=id),
            # FIGURE OUT HOW TO BE DRY YO
            'twitter_followers': SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['followers_count'],
            'twitter_name': SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['name'],
            'twitter_screen': SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['screen_name'],
            # 'twitter_email': SocialAccount.objects.filter(user=request.user, provider='twitter')[0].extra_data['email'],
        }
    return render(request, 'users/profile.html', context)

# >>> user1[12].post.id
@login_required
def update_user_profile(request):
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
        context = {
            'p_form': p_form,
        }
        return render(request, 'users/update_profile.html', context)

# Consider making a new view and template to submit multiple photos


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