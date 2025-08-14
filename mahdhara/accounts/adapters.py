# # myapp/adapters.py
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
#
# class MySocialAccountAdapter(DefaultSocialAccountAdapter):
#     def pre_social_login(self, request, sociallogin):
#         # Only set role if new user
#         if sociallogin.is_new:
#             # Check if session has instructor signup
#             signup_role = request.session.pop("signup_role", None)
#             if signup_role:
#                 sociallogin.user.role = signup_role
#             else:
#                 # Default role for students
#                 sociallogin.user.role = "student"


from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        role = request.session.pop("signup_role", None)
        if role and not sociallogin.user.pk:
            sociallogin.user.role = role
