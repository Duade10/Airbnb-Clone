from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    # help = "This command says it loves you"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="How many times do you want to show i love you")

    def handle(self, *args, **options):
        amenities = [
            "Air Conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Essentials",
            "Toilet",
            "Wifi",
            "Microwave",
            "Kitchen",
            "Washer",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
            "Features",
            "Pool",
            "Hot tub",
            "Free parking on premises",
            "EV charger",
            "Crib",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Beachfront",
            "Waterfront",
            "Ski-in/ski-out",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]
        for i in amenities:
            room_models.Amenity.objects.create(name=i)
        self.stdout.write(self.style.SUCCESS("Amenities Created"))
