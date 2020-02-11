from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('donate/charge/', views.charge, name='charge'),
    path('donate/', views.HomePageView.as_view(), name='donate'),
]