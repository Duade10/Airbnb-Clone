from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "birthdate",
        "currency",
        "is_staff",
        "is_superuser",
        "superhost",
    )
    # list_filter = ("superhost", "language", "currency")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom User Fields",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "birthdate",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
