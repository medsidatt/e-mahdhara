
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        role = request.session.pop("signup_role", None)
        if role and not sociallogin.user.pk:
            sociallogin.user.role = role
