from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from sole.core.constants import PAGINATION_NUMBER
from sole.glimpses.models import Glimpse
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


class ProfileView(ListView):
    model = Glimpse
    ordering = "-creation_datetime"
    context_object_name = "glimpses"
    template_name = "glimpse_list.html"
    paginate_by = PAGINATION_NUMBER

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        queryset = super().get_queryset().filter(author=user_id)

        if user_id == self.request.user.id and self.request.GET.get("draft"):
            queryset = queryset.filter(status=Glimpse.Status.DRAFT)
        elif user_id == self.request.user.id:
            queryset = queryset.exclude(status=Glimpse.Status.DRAFT)
        else:
            # TODO
            user = get_object_or_404(User, pk=user_id)
            following_user_ids = list(user.following.all().values_list("id", flat=True))
            queryset = queryset.filter(author__in=following_user_ids).exclude(status=Glimpse.Status.DRAFT)

        return queryset
