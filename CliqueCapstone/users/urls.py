from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/', views.create_photo_post, name='profile'),
]