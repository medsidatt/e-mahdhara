from django.shortcuts import redirect

def instructor_signup(request):
    request.session["signup_role"] = "cheikh"
    return redirect("/accounts/google/login/")