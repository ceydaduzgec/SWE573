from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostListView,
    PostUpdateView,
    like,
    rate,
)

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("update/<int:post_id>/", PostUpdateView.as_view(), name="update"),
    path("delete/<int:post_id>/", PostDeleteView.as_view(), name="delete"),
    path("like/<int:post_id>/", like, name="like"),
    path("rate/<int:post_id>/", rate, name="rate"),
]
