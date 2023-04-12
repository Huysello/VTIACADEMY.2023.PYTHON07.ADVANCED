from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person


def index(request):
    return HttpResponse("This is my first Django application")

def person_list(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'person_list.html', context)