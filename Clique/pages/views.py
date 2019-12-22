from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return render(request, 'pages/welcome.html')

def home_page(request):
    return render(request, 'pages/home.html')

def search_page(request):
    return render(request, 'pages/search_page.html')