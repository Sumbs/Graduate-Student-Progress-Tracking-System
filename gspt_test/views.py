from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gspt_test/index.html')

def homepage(request):
    return render(request, 'gspt_test/homepage.html')

def login(request):
    return render(request, 'gspt_test/login.html')

def curriculumchecklist(request):
    return render(request, 'gspt_test/curriculumchecklist.html')