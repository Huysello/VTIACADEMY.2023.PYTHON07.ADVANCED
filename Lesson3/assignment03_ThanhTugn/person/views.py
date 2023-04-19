from django.shortcuts import render
from .models import Person

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person/person_list.html', {'persons': persons})
