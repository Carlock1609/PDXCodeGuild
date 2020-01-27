from django import forms
import django_filters
from .models import UserProfile

class UserFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains')
    follower_amount = django_filters.NumberFilter(field_name='follower_amount', lookup_expr=int)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'follower_amount']

    