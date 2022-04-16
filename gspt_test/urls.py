from django.urls import path

from . import views

app_name = 'gspt_test'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('students', views.students, name = 'students'),
    path('checklist', views.checklist, name = 'checklist'),
]