from django import forms
from .models import Person, Enrollment

class EnrollmentCreateForm(forms.ModelForm):
    student_no = forms.ModelChoiceField(queryset=Person.objects.all(), disabled=True)

    class Meta:
        model = Enrollment
        fields = '__all__'