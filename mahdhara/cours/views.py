from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from .models import Cours
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Cours


class ListeCoursView(LoginRequiredMixin, ListView):
    model = Cours
    template_name = 'cours/liste.html'
    context_object_name = 'cours'


from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from cours.models import Cours
from student.models import Enrollment

class CourseDetailView(DetailView):
    model = Cours
    template_name = "cours/detail.html"
    context_object_name = "course"
    pk_url_kwarg = "course_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated and getattr(user, "role", None) != "cheikh":
            context['enrolled'] = Enrollment.objects.filter(student=user, cours=self.object).exists()
        else:
            context['enrolled'] = False
        return context



class CoursCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Cours
    fields = ['titre', 'description', 'prix']
    template_name = 'cours/form.html'
    success_url = reverse_lazy('liste_cours')

    def form_valid(self, form):
        # Assigne le créateur (Cheikh) automatiquement
        form.instance.createur = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Seuls les Cheikhs peuvent créer un cours
        return self.request.user.role == 'cheikh'


class CoursUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cours
    fields = ['titre', 'description', 'prix']
    template_name = 'cours/form.html'
    success_url = reverse_lazy('liste_cours')

    def test_func(self):
        # Seuls le créateur du cours (Cheikh) peut modifier
        cours = self.get_object()
        return self.request.user == cours.createur


class CoursDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cours
    template_name = 'cours/confirm_delete.html'
    success_url = reverse_lazy('liste_cours')

    def test_func(self):
        # Seuls le créateur du cours (Cheikh) peut supprimer
        cours = self.get_object()
        return self.request.user == cours.createur

