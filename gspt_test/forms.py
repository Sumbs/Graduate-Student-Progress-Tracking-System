from django import forms
from .models import Person, Enrollment

class EnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Person.objects.all(), disabled=True)

    class Meta:
        model = Enrollment
        fields = '__all__'