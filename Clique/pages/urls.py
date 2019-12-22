from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('home/', views.home_page, name='home_page'),
    path('search/', views.search_page, name='search_page'),
]