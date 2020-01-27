from django.urls import path
from django_filters.views import FilterView
from .filters import UserFilter
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', FilterView.as_view(filterset_class=UserFilter, template_name='pages/search.html'), name='search'),
]