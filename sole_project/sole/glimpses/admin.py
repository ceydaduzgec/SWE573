from django.contrib import admin
from django.db.models import Count

from .models import Like, Glimpse, Rating, Tag

admin.site.site_header = "sole Admin"
admin.site.index_title = "Welcome to sole"


class GlimpseInlineAdmin(admin.TabularInline):
    model = Glimpse

    def has_delete_permission(self, request, obj=None):  # can be written as tihs
        return False

    def has_add_permission(self, *args, **kwargs):  # or this
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


@admin.register(Glimpse)
class GlimpsesAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Glimpse Information",
            {
                "fields": (
                    "title",
                    "url",
                    "text",
                    "status",
                    "created_by",
                    "creation_datetime",
                )
            },
        ),
        (
            "Activities Information",
            {
                "fields": (
                    "tags",
                    "liked_by",
                    "rating",
                    "comments"
                )
            },
        ),
    )

    list_display = ("title", "creation_datetime", "glimpse_like_count",)
    list_select_related = ("created_by",)
    list_filter = ("tags", "creation_datetime", "created_by",)
    readonly_fields = ("created_by", "creation_datetime", "glimpse_like_count",)

    def glimpse_like_count(self, obj):
        return obj.glimpse_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(glimpse_count=Count("liked_by"))
        return queryset


admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Rating)
