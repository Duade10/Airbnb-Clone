from django.contrib import admin
from .models import Review

# REVIEW MODEL ADMIN DEFINTION
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("__str__", "rating_average")
