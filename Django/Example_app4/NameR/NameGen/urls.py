from django.urls import path
from . import views

app_name = "NameGen"

urlpatterns = [
    path('', views.index.as_view()),
    path('results/', views.ResultsView.as_view()),
]