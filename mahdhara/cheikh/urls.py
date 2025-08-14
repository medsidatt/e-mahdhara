from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="manage_courses"),
    path("courses/create/", views.CourseCreateView.as_view(), name="course_create"),
    path("courses/<int:pk>/edit/", views.CourseUpdateView.as_view(), name="course_edit"),
    path("courses/<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course_delete"),
]
