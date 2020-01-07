from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('community/', views.community, name='community'),
]