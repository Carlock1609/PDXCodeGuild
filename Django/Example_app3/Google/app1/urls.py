from django.urls import path, include
from . import views

# FROM . IMPORT VIEWS GETS THE PATH

# SERVER RECIEVES REQUEST TO /about
# THEN URL FIGURESOUT WHICH FUNCTION TO FIRE TO VIEWS
# IN THIS CASE INDEX
urlpatterns = [
    path('', views.index)
]