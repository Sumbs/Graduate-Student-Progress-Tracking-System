from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'gspt_test'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login, name = 'login'),
    path('curriculumchecklist/', views.curriculumchecklist, name = 'curriculumchecklist'),
]

urlpatterns += staticfiles_urlpatterns()