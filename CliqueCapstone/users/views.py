from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, reverse

from django.contrib.auth.decorators import login_required # Decorators
from django.contrib.auth import authenticate, login # More authentication
# from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms

from .models import CustomUser, UserProfile, ProfilePhotos, ProfileLibrary, FriendRequest
from allauth.socialaccount.models import SocialAccount
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.forms import modelformset_factory

from django.contrib import messages
import boto3
from django.core.files.storage import FileSystemStorage
from decouple import config

# , ProfileUserPost, ProfileUserPhoto
# , PostForm, PhotoForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
@login_required
def profile_page(request, id):
    # Multiple Photo posts
    user_id = request.user.id
    if request.method == 'POST':
        # print(request.FILES)
        image_file = request.FILES.get('image_file')
        image_type = request.POST.get('image_type')
        upload = ProfilePhotos(
            file=image_file,
            user=request.user
        )
        upload.save()
        image_url = upload.file.url

        return redirect(f'/users/profile/{user_id}/')
    else:
        # postForm = PostForm()
        # # Research queryset
        # formset = ImageFormSet(queryset=ProfileUserPhoto.objects.none())
        # user_id = request.user.id
        create_msg = UserProfile.objects.get(user=CustomUser.objects.get(id=id))
        images = ProfilePhotos.objects.filter(user=request.user)
        friends = FriendRequest.objects.filter(from_user_id=id).count()

        profile = UserProfile.objects.get(user=CustomUser.objects.get(id=id))
        profile.follower_amount = SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['followers_count']
        profile.first_name = SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['name']
        profile.location = SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['location']
        profile.save()

        context = {
            'friends': friends,
            'images': images,
            'create_msg': create_msg,
            'auth': CustomUser.objects.get(id=id),
            # 'postForm': postForm,
            # 'formset': formset,
            'user_profile': UserProfile.objects.get(id=UserProfile.objects.get(user=CustomUser.objects.get(id=id)).id),
            # 'library': ProfileUserPhoto.objects.get(id=id),
            # FIGURE OUT HOW TO BE DRY YO
            # 'twitter_followers': SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['followers_count'],
            # 'twitter_name': SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['name'],
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
    user_id = request.user.id

    if request.method == 'POST':
        # UserProfile.profile_picture # why are these here? Test this to see
        # UserProfile.cover_picture
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # FIX THIS!!!
            return redirect(f'/users/profile/{user_id}/')
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.user)
        context = {
            'p_form': p_form,
        }
        return render(request, 'users/update_profile.html', context)

# AWS S3 VIEWS
@login_required
def delete_image(request, id):
    user_id = request.user.id
    image = ProfilePhotos.objects.get(id=id)

    s3 = boto3.resource(
        's3',
        aws_access_key_id = config("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
    )

    s3.Object('django-clique-files', f'{image.file.name}').delete()
    image.delete()
    return redirect(f'/users/profile/{user_id}/')
    
@login_required
def photo_library_page(request):
    return render(request, 'users/photo_library.html')


def friends_list_page(request, id):
    user_id = request.user.id
    # user = request.user

    from_id = CustomUser.objects.get(id=user_id)
    to_id = CustomUser.objects.get(id=id)

    if request.method == 'POST':
        add = FriendRequest(
            from_user=from_id,
            to_user=to_id,
        )
        add.save()
        
        return redirect(f'/users/profile/{id}/')
    else:
        # This is only return one sense i specifide it
        friends = FriendRequest.objects.filter(from_user=id)
        users_list = CustomUser.objects.get(id=id)

        context = {
            'users_list': users_list,
            'friends': friends,
            # 'friends': FriendRequest.objects.filter(from_user=user_id),
        }
        return render(request, 'users/friends_list.html', context)

# >>> FriendRequest.objects.filter(from_user=7)[0].to_user
# <CustomUser: Carlock1609>
# >>> FriendRequest.objects.filter(from_user=7)[0].to_user.user
# <UserProfile: Carlock1609's Profile>

# def add_friend(request, id):
#     user_id = request.user.id
#     friend_id = CustomUser.objects.get(id=UserProfile.objects.get(id=id).user.id)
#     user = UserProfile.objects.get(user_id=user_id)

#     if request.method == 'POST':
#         add_friend_btn = request.POST['friends_list']
#         update = user(
#             friends_list=add_friend_btn,
#         )
#         update.save()
# NOT WORKING!
    # user.Object(friend_id).add() 

        # profile.follower_amount = SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['followers_count']
        # profile.first_name = SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['name']
        # profile.location = SocialAccount.objects.filter(user=CustomUser.objects.get(id=id), provider='twitter')[0].extra_data['location']
        # profile.save()
    # user.save()


    # return redirect(f'/users/profile/{friend_id}/')


# class SnippetDetailView(DetailView):
#     model = UserProfile

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