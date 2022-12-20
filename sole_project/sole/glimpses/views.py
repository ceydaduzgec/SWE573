from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from sole.core.constants import PAGINATION_NUMBER

from .models import Glimpse, Like


class OwnerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        glimpse = get_object_or_404(Glimpse, pk=self.kwargs.get("glimpse_id"))
        if glimpse.author != request.user:
            messages.error(request, "You are not the owner of this glimpse!")
            return redirect("users:login")
        return super().dispatch(request, *args, **kwargs)


class GlimpseListView(ListView):
    model = Glimpse
    ordering = "-creation_datetime"
    context_object_name = "glimpses"
    template_name = "glimpse_list.html"
    paginate_by = PAGINATION_NUMBER

    def get_template_names(self):
        if self.request.GET.get("username"):
            return ["user_profile.html"]
        else:
            return ["glimpse_list.html"]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get("status") == "draft":
            queryset = queryset.filter(status=Glimpse.Status.DRAFT)
        elif self.request.GET.get("status") == "private":
            queryset = queryset.filter(status=Glimpse.Status.PRIVATE)
        else:
            queryset = queryset.filter(status=Glimpse.Status.PUBLIC)

        if username := self.request.GET.get("username"):
            queryset = queryset.filter(author__username=username)

        if tag := self.request.GET.get("tag"):
            queryset = queryset.filter(tags__name=tag)

        if query := self.request.GET.get("q"):
            queryset = Glimpse.objects.allowed_glimpses.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(url__icontains=query)
                | Q(author__username__icontains=query)
            )

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class GlimpseCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Glimpse
    template_name = "create_glimpse.html"
    fields = ["url", "title", "description", "tags", "category", "status"]
    success_message = "Glimpse was created successfully"
    success_url = reverse_lazy("glimpses:list")
    pk_url_kwarg = "glimpse_id"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class GlimpseUpdateView(SuccessMessageMixin, OwnerRequiredMixin, UpdateView):
    model = Glimpse
    context_object_name = "glimpse"
    template_name = "update_glimpse.html"
    fields = ["url", "title", "description", "tags", "status"]
    success_message = "Glimpse was updated successfully"
    success_url = reverse_lazy("glimpses:list")
    pk_url_kwarg = "glimpse_id"


class GlimpseDeleteView(SuccessMessageMixin, OwnerRequiredMixin, DeleteView):
    model = Glimpse
    context_object_name = "glimpse"
    template_name = "update_glimpse.html"
    success_message = "Glimpse was deleted successfully"
    success_url = reverse_lazy("glimpses:list")
    pk_url_kwarg = "glimpse_id"


@login_required()
def like(request, glimpse_id, *args, **kwargs):

    if request.method == "POST":
        glimpse = get_object_or_404(Glimpse, pk=glimpse_id)
        like, created = Like.objects.get_or_create(glimpse=glimpse, user=request.user)

        if not created:
            like.delete()
        return redirect("glimpses:list")

    else:
        # need a warning here
        return redirect("glimpses:list")
