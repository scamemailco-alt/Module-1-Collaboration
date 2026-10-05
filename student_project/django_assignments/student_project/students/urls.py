from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form, name='student_form'),
    path('results/', views.student_results, name='student_results'),
]