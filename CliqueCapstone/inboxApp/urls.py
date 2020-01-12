from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.user_inbox, name='user-inbox'),
    path('message/<int:id>/', views.user_msg, name='user-msg'),
]