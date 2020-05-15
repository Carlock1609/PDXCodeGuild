from django.shortcuts import render, redirect


from .models import BookInstance

def list_books(request):  
  all_books = BookInstance.objects.all()
  context = {
    'all_books': all_books,
  }
  return render(request, 'catalog/book_list.html', context = context)

def book_details(request, id):
  book = BookInstance.objects.filter(pk = id)
  return render(request, 'catalog/book_details', context = context)

def return_book(request, id):
  book = BookInstance.objects.get(id = id)
  book.check_in()
  book.save()
  return redirect('dashboard')

def loan_book(request, id):
  book = BookInstance.objects.get(id = id)
  book.check_out(request.user)
  book.save()
  return redirect('dashboard')
  
