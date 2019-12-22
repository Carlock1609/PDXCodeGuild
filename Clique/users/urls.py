from django.urls import path
from . import views

# urlpattern here

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('register/', views.register_page, name='register_page'),
    path('profile/', views.profile_page, name='profile_page'),
]