from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="How many times do you want to show i love you")

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for i in facilities:
            room_models.Facility.objects.create(name=i)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)}  facilities created! "))
