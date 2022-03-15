from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gspt_test/index.html')