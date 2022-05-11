from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
class Degree_Program(models.Model):
    deg_program_id = models.AutoField(primary_key=True)
    deg_program_name = models.CharField(max_length=100)

    def __str__(self):
        return self.deg_program_name

class Specialization(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.spec_name

class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=100)

    def __str__(self):
        return self.lab_name

class Person(models.Model):
    person_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree_program = models.ForeignKey(Degree_Program, on_delete=models.RESTRICT)
    year_initial = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    sem_initial = models.CharField(
        max_length = 1,
        choices = [("1", "1st Semester"), ("2", "2nd Semester"), ("3", "Midyear")],
        default = "1",
    )
    years_to_grad = models.IntegerField()
    current_specialization = models.ForeignKey(Specialization, on_delete=models.RESTRICT, related_name="current_spec")
    previous_specialization = models.ForeignKey(Specialization, on_delete=models.RESTRICT, related_name="prev_spec")
    lab_affiliation = models.ForeignKey(Lab, on_delete=models.RESTRICT)
    adviser = models.ForeignKey('self', null=True, blank=True, on_delete=models.RESTRICT)
    is_professor = models.BooleanField()
    study_plan = models.CharField(
        max_length = 1,
        choices = [("1", "Full-time"), ("2", "Part-time"), ("3", "Non-Degree")],
        default = "1",
    )
    gwa = models.DecimalField(max_digits=5, decimal_places=2)
    units_taken = models.DecimalField(max_digits=4, decimal_places=1)
    units_required = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def year_standing(self):
        return str(5 - self.years_to_grad)
    
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    lab = models.ForeignKey(Lab, on_delete=models.RESTRICT)
    units = models.IntegerField()
    title = models.CharField(max_length=50)
    kind = models.CharField(
        max_length = 1,
        choices = [("1", "Core"), ("2", "Specialization"), ("3", "Elective")]
    )

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Person, on_delete=models.RESTRICT)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    grade = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    remark = models.CharField(
        null = True,
        blank = True,
        max_length = 1,
        choices = [("1", "Pass"), ("2", "INC"), ("3", "DRP")],
    )
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(3000)],)
    sem = models.CharField(
        max_length = 1,
        choices = [("1", "1st Semester"), ("2", "2nd Semester"), ("3", "Midyear")],
        default = "1",
    )

    def __str__(self):
        return f"{self.course} ({self.get_semester()}, {self.acad_year()}): {self.student}"
    
    def acad_year(self):
        return f"{self.year}-{self.year + 1}"

    def get_semester(self):
        sem = self.sem
        if sem == "1":
            return "1st Semester"
        elif sem == "2":
            return "2nd Semester"
        else:
            return "Midyear"
    
    def get_absolute_url(self):
        return reverse('gspt_test:study_plan', kwargs={'person_id': self.student_no.person_id})
        

class Prereq(models.Model):
    current_course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    prerequisite_course = models.ForeignKey(Course, on_delete=models.RESTRICT),

class Coreq(models.Model):
    current_course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    corequisite_course = models.ForeignKey(Course, on_delete=models.RESTRICT),
