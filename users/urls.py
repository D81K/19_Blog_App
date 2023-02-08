from django.urls import include, path
from .views import register, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
]