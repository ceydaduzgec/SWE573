from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import RateForm
from .models import Like, Post, Rate, Tag


class OwnerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        if post.created_by != request.user:
            messages.error(request, "You are not the owner of this post!")
            return redirect("users:login")
        return super().dispatch(request, *args, **kwargs)


class PostListView(ListView):
    model = Post
    ordering = "-creation_datetime"
    context_object_name = "posts"
    template_name = "post_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if username := self.request.GET.get("username"):
            queryset = queryset.filter(created_by__username=username)
        if tag := self.request.GET.get("tag"):
            queryset = queryset.filter(tags__name=tag)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tags"] = Tag.most_used_tags()
        context["rate_form"] = RateForm()
        return context


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ["image", "text", "tags"]
    success_message = "Post was shared successfully"
    success_url = reverse_lazy("posts:list")
    pk_url_kwarg = "post_id"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, OwnerRequiredMixin, UpdateView):
    model = Post
    context_object_name = "post"
    template_name = "update_posts.html"
    fields = ["text", "tags"]
    success_message = "Post was updated successfully"
    success_url = reverse_lazy("posts:list")
    pk_url_kwarg = "post_id"


class PostDeleteView(SuccessMessageMixin, OwnerRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "update_posts.html"
    success_message = "Post was deleted successfully"
    success_url = reverse_lazy("posts:list")
    pk_url_kwarg = "post_id"


@login_required()
def like(request, post_id, *args, **kwargs):

    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            like.delete()
        return redirect("posts:list")

    else:
        # need a warning here
        return redirect("posts:list")


@login_required()
def rate(request, post_id, *args, **kwargs):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate, _ = Rate.objects.update_or_create(
                post__id=post_id,
                user=request.user,
                defaults={"rating": form.instance.rating},
            )
            return redirect("posts:list")
