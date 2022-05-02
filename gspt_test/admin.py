from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Degree_Program)
admin.site.register(Specialization)
admin.site.register(Lab)
admin.site.register(Enrollment)
