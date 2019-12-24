from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('redirecting/<int:code>', views.redirecting, name='redirecting'),
]