from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_inbox, name='user-inbox'),
    path('direct/', views.direct_msg, name='direct-msg'),
]