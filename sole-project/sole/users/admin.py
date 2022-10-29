from django.contrib import admin
from django.contrib.auth import get_user_model
from sole.posts.admin import PostInlineAdmin


class UsersAdmin(admin.ModelAdmin):
    inlines = [PostInlineAdmin]
    list_display = ("username", "last_login", "date_joined")
    list_filter = ("is_staff", "is_active", "last_login", "date_joined")
    readonly_fields = ("last_login", "date_joined")
    exclude = ("first_name", "last_name", "groups", "user_permissions", "password")


admin.site.register(get_user_model(), UsersAdmin)
