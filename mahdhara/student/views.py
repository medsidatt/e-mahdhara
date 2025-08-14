from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Enrollment

@login_required
def my_learning(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, "student/my_learning.html", {"enrollments": enrollments})

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cours.models import Cours
from student.models import Enrollment

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Cours, id=course_id)
    # Create enrollment if it doesn't exist
    Enrollment.objects.get_or_create(student=request.user, cours=course)
    return redirect("my_learning")  # redirect to student's learning dashboard

