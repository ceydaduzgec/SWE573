from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from sole.users.views import PasswordChangeView, SignUpView

app_name = "users"

urlpatterns = [
    path("profile/", SignUpView.as_view(), name="profile"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/", PasswordChangeView.as_view(), name="change_password"),
]
