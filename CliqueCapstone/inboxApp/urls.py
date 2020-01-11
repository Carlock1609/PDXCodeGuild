from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.user_inbox, name='user-inbox'),
    path('direct/<int:id>/', views.direct_msg, name='direct-msg'),
]