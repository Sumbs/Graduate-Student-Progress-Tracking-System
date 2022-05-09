from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'gspt_test'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('students', views.students, name = 'students'),
    path('students/<int:person_id>/', views.study_plan, name = 'study_plan'),
    path('checklist', views.checklist, name = 'checklist'),
    path('login', views.loginUser, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
]

urlpatterns += staticfiles_urlpatterns()