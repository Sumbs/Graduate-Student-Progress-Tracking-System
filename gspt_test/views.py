from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    return render(request, 'gspt_test/index.html')

def students(request):
    people = Person.objects.all()
    context = {"people": people}

    return render(request, 'gspt_test/students.html', context)

def study_plan(request, person_id):
    enrollments = Enrollment.objects.select_related('course_id').filter(student_no=person_id)

    context = {"enrollments": enrollments}

    return render(request, 'gspt_test/study_plan.html', context)

def checklist(request):
    return render(request, 'gspt_test/checklist.html')