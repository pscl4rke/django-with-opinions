

from django.contrib.auth.apps import AuthConfig as DjangoAuthConfig


class AuthConfig(DjangoAuthConfig):

    # This fixes the American spelling:
    verbose_name = "Authentication and Authorisation"
