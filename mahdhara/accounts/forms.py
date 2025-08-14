#
# from allauth.account.forms import SignupForm
# from django import forms
#
# class InstructorSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Remove all default help texts
#         for field_name in self.fields:
#             self.fields[field_name].help_text = None
#         # Optional: Rename labels
#         self.fields['email'].label = "Email"
#         self.fields['password1'].label = "Password"
#         self.fields['password2'].label = "Confirm Password"
#
#     def save(self, request):
#         user = super().save(request)
#         user.role = "cheikh"  # instructor role
#         user.save()
#         return user

# accounts/forms.py
from allauth.account.forms import SignupForm
from django import forms

class InstructorSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help texts and default instructions
        for field_name, field in self.fields.items():
            field.help_text = None
            field.label = field.label.capitalize()  # Optional: capitalize labels

        # Optional: Customize specific labels
        self.fields['email'].label = "Email"
        self.fields['username'].label = "Username"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

    def save(self, request):
        user = super().save(request)
        user.role = "cheikh"  # Set instructor role
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


# accounts/forms.py
class StudentSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = None
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

    def save(self, request):
        user = super().save(request)
        user.role = "student"  # student role
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

