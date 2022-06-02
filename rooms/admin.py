from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# CONFIGURE ROOMTYPE, FACILITY, HOUSERULE, AMENITY MODEL TO ADMIN
@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


# ADMINISTRATING PHOTOS ADMIN AS INLINE MODEL ADMIN FOR ROOMS ADMIN
class PhotoInline(admin.TabularInline):
    model = models.Photo


# CONFIGURE ROOM MODEL TO ADMIN
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "city", "address", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("beds", "baths", "bedrooms", "guests")}),
        ("More about the spaces", {"classes": ("collapse",), "fields": ("amenities", "facilities", "house_rules")}),
        ("Last details", {"fields": ("host",)}),
    )

    ordering = ("name", "price")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    list_filter = (
        "host__superhost",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    raw_id_fields = ("host",)
    search_fields = ("country", "city", "host__username", "name")
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos"


# CONFIGURE PHOTO MODEL TO ADMIN
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' height='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
