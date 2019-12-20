from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list_todos, name='list'),
    path('add/', views.add_todo, name="add"),
    path('remove/<int:id>', views.remove_todo, name='remove'),
    path('update/<int:id>', views.update, name='update'),
    path('mark/<int:id>', views.mark, name='mark'),
    path('detail/<int:id>', views.detail, name='detail'), 
]
