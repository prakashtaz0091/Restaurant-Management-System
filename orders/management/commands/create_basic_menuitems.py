from django.core.management.base import BaseCommand
from django.db import transaction

from orders.data.basic_menu_items import (
    KITCHEN_STATIONS,
    RESTAURANT_MENU_ITEMS,
)
from orders.models import (
    Category,
    MenuItem,
    KitchenStation,
)


class Command(BaseCommand):
    help = "Populate kitchen stations, categories and menu items"

    @transaction.atomic
    def handle(self, *args, **options):
        stations_created = 0
        categories_created = 0
        items_created = 0

        # ------------------------------------------------------------------
        # Create Kitchen Stations
        # ------------------------------------------------------------------
        for code, station_data in KITCHEN_STATIONS.items():
            _, created = KitchenStation.objects.get_or_create(
                code=code,
                defaults={
                    "name": station_data["name"],
                },
            )

            if created:
                stations_created += 1

        # ------------------------------------------------------------------
        # Create Categories & Menu Items
        # ------------------------------------------------------------------
        for category_name, items in RESTAURANT_MENU_ITEMS.items():

            # Drinks contains nested subcategories
            if isinstance(items, dict):

                Category.objects.get_or_create(
                    name=category_name.title()
                )

                for subcategory_name, sub_items in items.items():

                    category, created = Category.objects.get_or_create(
                        name=f"{category_name.title()} - {subcategory_name.title()}"
                    )

                    if created:
                        categories_created += 1

                    for item in sub_items:
                        station = KitchenStation.objects.get(
                            code=item["station"]
                        )

                        _, created = MenuItem.objects.get_or_create(
                            category=category,
                            name=item["name"],
                            defaults={
                                "price": item["price"],
                                "default_priority": item["priority"],
                                "est_time": item["est_time"],
                                "station": station,
                            },
                        )

                        if created:
                            items_created += 1

            else:
                category, created = Category.objects.get_or_create(
                    name=category_name.title()
                )

                if created:
                    categories_created += 1

                for item in items:
                    station = KitchenStation.objects.get(
                        code=item["station"]
                    )

                    _, created = MenuItem.objects.get_or_create(
                        category=category,
                        name=item["name"],
                        defaults={
                            "price": item["price"],
                            "default_priority": item["priority"],
                            "est_time": item["est_time"],
                            "station": station,
                        },
                    )

                    if created:
                        items_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"""
Seeding completed successfully.

Kitchen Stations Created: {stations_created}
Categories Created:       {categories_created}
Menu Items Created:       {items_created}
                """.strip()
            )
        )