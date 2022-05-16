from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person, Enrollment, Course
from .forms import EnrollmentForm


# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('gspt_test:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = authenticate(request, username=User.objects.get(email=username), password=password)
        except:
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
    
class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'gspt_test:login'
    redirect_field_name = 'next'
    model = Enrollment
    form_class = EnrollmentForm

    def get_initial(self):
        initial = super().get_initial()
        initial['student'] = Person.objects.get(pk=self.kwargs['pk'])
        return initial
    
class EnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'gspt_test:login'
    redirect_field_name = 'next'
    model = Enrollment
    form_class = EnrollmentForm
    template_name_suffix = '_update_form'

    def get_object(self):
        return self.model.objects.get(
            student=self.kwargs['pk'],
            course=self.kwargs['course_id'],
            year=self.request.GET['year'],
            sem=self.request.GET['sem'],
        )


class EnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'gspt_test:login'
    redirect_field_name = 'next'
    model = Enrollment

    def get_object(self):
        return self.model.objects.get(
            student=self.kwargs['pk'],
            course=self.kwargs['course_id'],
            year=self.request.GET['year'],
            sem=self.request.GET['sem'],
        )

    def get_success_url(self):
        return reverse_lazy('gspt_test:study_plan', kwargs={'person_id': self.object.student.person_id})


@login_required(login_url='gspt_test:login')
def checklist(request):
    return render(request, "gspt_test/checklist.html")

@login_required(login_url='gspt_test:login')
def home(request):
    return render(request, "gspt_test/home.html")

class change_password(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    login_url = 'gspt_test:login'
    redirect_field_name = 'next'
    template_name = 'gspt_test/change_password.html'
    success_url = reverse_lazy('gspt_test:home')
    success_message = 'Password Changed Succesfully!'

