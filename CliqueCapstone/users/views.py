from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserProfile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms

from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# DONT LET USERS CHANGE USERNAMES
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

@login_required # only logged in users can view this
def edit_user(request, pk):
    # query the CustomerUser boject with pk from url
    user = CustomUser.objects.get(pk=pk)

    # Prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(CustomUser, UserProfile, fields=('first_name', 'social_media', 'follower_amount', 'experience'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == 'POST':
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

            if formset.is_valid():
                created_user.save()
                formset.save()
                return HttpResponseRedirect('/accounts/profile/')
            
        return render(request, 'account/account_update/html', {
            'noodle': pk,
            'noodle_form': user_form,
            'formset': formset,
    })