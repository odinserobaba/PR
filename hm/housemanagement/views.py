from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
# Create your views here.


def index(request):
    person = Person.objects.all()
    data = {
        'person': person,
    }
    return render(request, 'housemanagement/index.html', context=data)


def home(request):
    return HttpResponse("HOME")


def about(request):
    return HttpResponse("ABOUT")
