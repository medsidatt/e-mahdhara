from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from cours.models import Cours

class CheikhRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == "cheikh"

class DashboardView(LoginRequiredMixin, CheikhRequiredMixin, TemplateView):
    template_name = "cheikh/dashboard.html"

class CourseListView(LoginRequiredMixin, CheikhRequiredMixin, ListView):
    model = Cours
    template_name = "cheikh/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Cours.objects.filter(createur=self.request.user)

class CourseCreateView(LoginRequiredMixin, CheikhRequiredMixin, CreateView):
    model = Cours
    fields = ["titre", "description", "est_gratuit", "prix"]
    template_name = "cheikh/course_form.html"
    success_url = reverse_lazy("manage_courses")

    def form_valid(self, form):
        form.instance.createur = self.request.user
        return super().form_valid(form)

class CourseUpdateView(LoginRequiredMixin, CheikhRequiredMixin, UpdateView):
    model = Cours
    fields = ["titre", "description", "est_gratuit", "prix"]
    template_name = "cheikh/course_form.html"
    success_url = reverse_lazy("manage_courses")

class CourseDeleteView(LoginRequiredMixin, CheikhRequiredMixin, DeleteView):
    model = Cours
    template_name = "cheikh/course_confirm_delete.html"
    success_url = reverse_lazy("manage_courses")
