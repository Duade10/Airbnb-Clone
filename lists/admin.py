from django.contrib import admin
from .models import List

# LIST MODEL ADMIN DEFINITION
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "count_rooms")

    search_fields = ("name",)

    filter_horizontal = ("rooms",)
