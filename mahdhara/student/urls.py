from django.urls import path
from . import views

urlpatterns = [
    path('my-learning/', views.my_learning, name='my_learning'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),

]
