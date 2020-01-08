from django.urls import path
from . import views


urlpatterns = [
    path('', views.UploadPhoto, name='upload'),
    path('profile/', views.profile, name='profile'),
]
