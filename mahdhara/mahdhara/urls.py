"""
URL configuration for mahdhara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from accounts.views import StudentSignupView
from cours.models import Cours
from accounts import views
from mahdhara.views import instructor_signup


class HomeView(ListView):
    model = Cours
    template_name = 'home.html'
    context_object_name = 'courses'
    ordering = ['-date_creation']


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/signup/', StudentSignupView.as_view(), name='account_signup'),

    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('cours/', include('cours.urls')),
    path("cheikh/", include("cheikh.urls")),
    path("instructor-signup/", views.instructor_signup_page, name="instructor_signup")

]
