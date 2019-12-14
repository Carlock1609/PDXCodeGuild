from django.shortcuts import render

# Create your views here.

# VIEWS RECIEVES URL'S PICKED FUNCTION AND FIRES RESPONSE HTML TO BROWSER
def index(request):
    return render(request, "index.html")