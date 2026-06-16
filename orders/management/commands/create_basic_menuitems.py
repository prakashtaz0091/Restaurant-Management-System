from django.core.management.base import BaseCommand
from django.db import transaction
from orders.data.basic_menu_items import RESTAURANT_MENU_ITEMS
from orders.models import Category, MenuItem


class Command(BaseCommand):
    help = "Populate basic menu categories and menu items"

    @transaction.atomic
    def handle(self, *args, **options):
        categories_created = 0
        items_created = 0

        for category_name, items in RESTAURANT_MENU_ITEMS.items():

            # drinks has nested categories
            if isinstance(items, dict):
                parent_category, _ = Category.objects.get_or_create(
                    name=category_name.title()
                )

                for subcategory_name, sub_items in items.items():
                    category, created = Category.objects.get_or_create(
                        name=f"{category_name.title()} - {subcategory_name.title()}"
                    )

                    if created:
                        categories_created += 1

                    for item in sub_items:
                        _, created = MenuItem.objects.get_or_create(
                            category=category,
                            name=item["name"],
                            defaults={
                                "price": item["price"],
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
                    _, created = MenuItem.objects.get_or_create(
                        category=category,
                        name=item["name"],
                        defaults={
                            "price": item["price"],
                        },
                    )

                    if created:
                        items_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. Categories created: {categories_created}, "
                f"Items created: {items_created}"
            )
        )