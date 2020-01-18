from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            'experience',
            'bio',
            'follower_amount', # SET UP API
            'social_media',
            'portfolio_links',
            'city',
            'state',
            'profile_picture',
            'cover_picture',
        ]

# DONT LET USERS CHANGE USERNAME
#  class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email']