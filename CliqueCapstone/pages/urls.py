from django.urls import path
from django_filters.views import FilterView
from .filters import UserFilter
from . import views
from django.contrib.auth import views as user_views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/list/$/', views.search, name='search'),
]