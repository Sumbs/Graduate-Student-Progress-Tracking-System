from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .models import Person, Enrollment
from .forms import EnrollmentForm

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('gspt_test:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('gspt_test:home')
        else:
            messages.warning(request, 'Username or Password is incorrect.')

    context = {}
    return render(request, 'gspt_test/login.html')

def logoutUser(request):
    logout(request)
    return redirect('gspt_test:login')

@login_required(login_url='gspt_test:login')
def index(request):
    return render(request, "gspt_test/index.html")


@login_required(login_url='gspt_test:login')
def students(request):
    people = Person.objects.all()
    context = {"people": people}

    return render(request, "gspt_test/students.html", context)


@login_required(login_url='gspt_test:login')
def study_plan(request, person_id):
    enrollments = (
        Enrollment.objects.select_related("course")
        .filter(student=person_id)
        .order_by("year", "sem")
    )

    student = Person.objects.get(pk=person_id)

    context = {
        "enrollments": enrollments,
        "student": student,
    }

    return render(request, "gspt_test/study_plan_sorted_by_sem.html", context)
    
class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm

    def get_initial(self):
        initial = super().get_initial()
        initial['student_no'] = Person.objects.get(pk=self.kwargs['pk'])
        return initial
    
class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm


@login_required(login_url='gspt_test:login')
def checklist(request):
    return render(request, "gspt_test/checklist.html")

@login_required(login_url='gspt_test:login')
def home(request):
    return render(request, "gspt_test/home.html")
