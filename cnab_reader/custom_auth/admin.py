from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from cnab_reader.custom_auth.models import CustomGroup
from cnab_reader.custom_auth.models import CustomUser


class UserAdmin(BaseUserAdmin):
    list_display = ("email", "first_name", "is_staff")
    search_fields = ("first_name", "email")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name",)}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(CustomGroup)
