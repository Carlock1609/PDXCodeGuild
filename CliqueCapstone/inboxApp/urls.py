from django.urls import path
from . import views


urlpatterns = [
    path('message_list/<int:id>/', views.user_inbox, name='user-inbox'),
    path('message/<int:id>/<str:conversation_name>/', views.user_msg, name='user-msg'),
    path('create_message/<int:id>/', views.create_msg, name='create-msg')
]