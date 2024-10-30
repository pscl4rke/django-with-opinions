

"""
URL configuration for {{ project_name }} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
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


from django.urls import include, path
from django.contrib import admin
import django.contrib.auth.views as auth_views

from . import views


handler404 = views.error_404
handler500 = views.error_500


auth_urlpatterns = [
    # The simplest way according to the docs is to import urlpatterns
    # from contrib.auth.urls, but that includes everything for password
    # changing and resetting, and those all use the contrib.admin page
    # themes, and it would be a right hassle to make the themes match.
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include((auth_urlpatterns, "auth"))),
    path("", views.home, name="home"),
]
