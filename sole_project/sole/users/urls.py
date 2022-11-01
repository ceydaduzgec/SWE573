from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from sole.users.views import SignUpView, change_password

app_name = "users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/", change_password, name="change_password"),
]
