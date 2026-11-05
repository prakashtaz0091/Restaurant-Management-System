from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User, Permission


GROUPS = ["kitchen_staff", "reception_staff"]
DEFAULT_PASS = "ASDFasdf@123"

class Command(BaseCommand):
    help = 'Creates Groups and Users objects in the database'

    def handle(self, *args, **options):
        for group_name in GROUPS:
            group, created = Group.objects.get_or_create(
                name=group_name
            )
            user = User.objects.create_user(
                username=f"{group_name}@123",
                password=DEFAULT_PASS,
                email="",
                first_name=group_name.title().split("_")[0],
                last_name=group_name.title().split("_")[1],
                is_staff=True
            )
            user.groups.add(group)
                    
            
        self.stdout.write(self.style.SUCCESS(f'Done'))   