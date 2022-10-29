from django.contrib import admin
from django.db.models import Count

from .models import Like, Post, Rate, Tag

admin.site.site_header = "sole Admin"
admin.site.index_title = "Welcome to sole"


class PostInlineAdmin(admin.TabularInline):
    model = Post

    def has_delete_permission(self, request, obj=None):  # can be written as tihs
        return False

    def has_add_permission(self, *args, **kwargs):  # or this
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Post information",
            {
                "fields": (
                    "image",
                    "text",
                    "created_by",
                    "creation_datetime",
                )
            },
        ),
        ("Activities information", {"fields": ("tags",)}),
    )

    list_display = ("text", "creation_datetime", "post_like_count")
    list_select_related = ("created_by",)
    list_filter = ("tags", "creation_datetime", "created_by")
    readonly_fields = ("created_by", "creation_datetime", "post_like_count")

    def post_like_count(self, obj):
        return obj.post_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(post_count=Count("likers"))
        return queryset


admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Rate)
