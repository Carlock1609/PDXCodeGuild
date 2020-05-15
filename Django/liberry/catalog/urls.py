from django.urls import path

from . import views

urlpatterns = [
  path('', views.list_books, name = 'list_books'),
  path('book_details/<slug:id>', views.book_details, name = 'book_details'),
  path('return_book/<slug:id>', views.return_book, name = 'return_book'),
  path('loan_book/<slug:id>', views.loan_book, name = 'loan_book'),
]