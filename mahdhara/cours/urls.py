from django.urls import path
from .views import (
    ListeCoursView,
    CoursCreateView,
    CoursUpdateView,
    CoursDeleteView,
    CourseDetailView,
)

urlpatterns = [
    path('', ListeCoursView.as_view(), name='liste_cours'),
path('<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
    path('ajouter/', CoursCreateView.as_view(), name='cours_ajouter'),
    path('modifier/<int:pk>/', CoursUpdateView.as_view(), name='cours_modifier'),
    path('supprimer/<int:pk>/', CoursDeleteView.as_view(), name='cours_supprimer'),
]
