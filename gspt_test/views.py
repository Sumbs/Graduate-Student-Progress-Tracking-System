from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
    return render(request, 'gspt_test/index.html')

def students(request):
    people = Person.objects.all()
    context = {"people": people}

    return render(request, 'gspt_test/students.html', context)

def checklist(request):
    return render(request, 'gspt_test/checklist.html')