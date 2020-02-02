from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile
#  ProfileUserPost, ProfileUserPhoto

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name')


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            # 'experience',
            'bio',
            'social_media',
            'portfolio_links',
            # 'location',
            # 'city',
            # 'state',
            'profile_picture',
            'cover_picture',
        ]

# class PostForm(forms.ModelForm):
#     title = forms.CharField(max_length=128)

#     class Meta:
#         model = ProfileUserPost
#         fields = [
#             'title'
#         ]

# class PhotoForm(forms.ModelForm):
#     image = forms.ImageField()

#     class Meta:
#         model = ProfileUserPhoto
#         fields = [
#             'image'
#         ]

        
# DONT LET USERS CHANGE USERNAME
#  class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email']