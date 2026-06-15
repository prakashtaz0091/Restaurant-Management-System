from django.core.management.base import BaseCommand
from orders.models import Table

class Command(BaseCommand):
    help = 'Helps to populate/seed/config restaurant tables'

    def add_arguments(self, parser):
        parser.add_argument('--n', type=int, help='No. of tables', default=10)

    def handle(self, *args, **options):
        no_of_tables = options.get('n')
        for number in range(1, no_of_tables+1):
            Table.objects.get_or_create(
                name=f"Table {number}",
                defaults={
                    'is_reserved':False
                }
            )
        
        self.stdout.write(self.style.SUCCESS(f'{no_of_tables} created successfully'))