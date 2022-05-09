from django.urls import path

from . import views

app_name = 'gspt_test'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('students', views.students, name = 'students'),
    path('students/<int:person_id>/', views.study_plan, name = 'study_plan'),
    path('checklist', views.checklist, name = 'checklist'),
]