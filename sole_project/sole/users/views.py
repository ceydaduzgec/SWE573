from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from sole.users.forms import SignUpForm
from sole.users.models import User


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("glimpses:list")

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "change_password.html"
    success_url = reverse_lazy("glimpses:list")
