from django.shortcuts import render
from .models import PersonLibrary

from django.views import generic
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, "index.html")

def ResultsView(generic.ListView):
    template_name = 'NameGen/results.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return PersonLibrary.objects.all()
