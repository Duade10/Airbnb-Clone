from django.db import models
from core.models import AbstractTimeStampedModel
from django_countries.fields import CountryField


class AbstractItem(AbstractTimeStampedModel):
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass

    class Meta:
        verbose_name = "Room Type"
        verbose_name_plural = "Room Types"
        ordering = ["-created"]


class Amenity(AbstractItem):
    pass

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    pass

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    pass

    class Meta:
        verbose_name = "HouseRule"
        verbose_name_plural = "House Rules"


class Photo(AbstractTimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(AbstractTimeStampedModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=150)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name="rooms", blank=True, null=True, on_delete=models.SET_NULL)
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for reviews in all_reviews:
                all_rating += reviews.rating_average()
                return all_rating / len(all_reviews)
        return 0
