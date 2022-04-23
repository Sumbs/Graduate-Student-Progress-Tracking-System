from django.db import models
from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Degree_Program(models.Model):
    deg_program_id = models.AutoField(primary_key=True)
    deg_program_name = models.CharField(max_length=100)

class Specialization(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=100)

class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.lab_name)

class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    lab_id = models.ForeignKey(Lab, on_delete=models.RESTRICT)

class Student(models.Model):
    student_no = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    program_id = models.ForeignKey(Degree_Program, on_delete=models.RESTRICT)
    year_initial = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    sem_initial = models.CharField(
        max_length = 1,
        choices = [("1", "1st Semester"), ("2", "2nd Semester"), ("3", "Midyear")],
        default = "1",
    )
    years_to_grad = models.IntegerField()
    curr_spec_id = models.ForeignKey(Specialization, on_delete=models.RESTRICT, related_name="current_spec")
    prev_spec_id = models.ForeignKey(Specialization, on_delete=models.RESTRICT, related_name="prev_spec")
    lab_id = models.ForeignKey(Lab, on_delete=models.RESTRICT)
    adviser_id = models.ForeignKey(Professor, on_delete=models.RESTRICT, null=True)
    study_plan = models.CharField(
        max_length = 1,
        choices = [("1", "Full-time"), ("2", "Part-time"), ("3", "Non-Degree")],
        default = "1",
    )
    
class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    lab_id = models.ForeignKey(Lab, on_delete=models.RESTRICT)
    title = models.CharField(max_length=50)
    kind = models.CharField(
        max_length = 1,
        choices = [("1", "Core"), ("2", "Specialization")]
    )

class Enrollment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.RESTRICT)
    student_no = models.ForeignKey(Student, on_delete=models.RESTRICT)
    grade = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True) # how about INC or DRP? ::resolved by proceeding field
    remark = models.CharField(
        null = True,
        blank = True,
        max_length = 1,
        choices = [("1", "pass"), ("2", "inc"), ("3", "drp")],
    )
    sem = models.CharField(
        max_length = 1,
        choices = [("1", "1st Semester"), ("2", "2nd Semester"), ("3", "Midyear")],
        default = "1",
    )

class Pre_req(models.Model):
    pre_course_id = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name="prereq"),
    new_course_id = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name="course")
