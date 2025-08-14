from allauth.account.views import SignupView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.urls import reverse


def instructor_signup_page(request):
    """
    Display instructor signup/login page with:
    - Email/password registration/login
    - Social account login
    """
    if request.method == "POST":
        form = InstructorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "cheikh"
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "account/instructor_signup.html", {"form": form})

# accounts/views.py
from django.views.generic import FormView
from accounts.forms import InstructorSignupForm
from django.urls import reverse_lazy

class InstructorSignupView(FormView):
    template_name = "accounts/instructor_signup.html"
    form_class = InstructorSignupForm
    success_url = reverse_lazy("account_login")

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)



from .forms import StudentSignupForm

class StudentSignupView(SignupView):
    form_class = StudentSignupForm

