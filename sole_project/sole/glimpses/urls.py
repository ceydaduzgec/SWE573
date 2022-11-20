from django.urls import path

from .views import (
    GlimpseCreateView,
    GlimpseDeleteView,
    GlimpseListView,
    GlimpseUpdateView,
    like,
    rate,
)

app_name = "glimpses"

urlpatterns = [
    path("", GlimpseListView.as_view(), name="list"),
    path("create/", GlimpseCreateView.as_view(), name="create"),
    path("update/<int:glimpse_id>/", GlimpseUpdateView.as_view(), name="update"),
    path("delete/<int:glimpse_id>/", GlimpseDeleteView.as_view(), name="delete"),
    path("like/<int:glimpse_id>/", like, name="like"),
    path("rate/<int:glimpse_id>/", rate, name="rate"),
]
