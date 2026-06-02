'''from django.urls import path
from . import views

urlpatterns = [
    path('grade/<int:marks>/', views.grade_view),
]'''
from django.urls import path
from . import views

urlpatterns = [
    #path('students/', views.student_list),
    path('students_form/', views.student_form),
]
