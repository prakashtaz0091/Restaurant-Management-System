from django.core.management.base import BaseCommand
from core.models import Table


class Command(BaseCommand):
    help = 'Creates Table objects in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--num',
            type=int,
            default=10,
            help='Number of tables to create (default: 10)',
        )

    def handle(self, *args, **options):
        count = options['num']
        for i in range(1, count + 1):
            table, created = Table.objects.get_or_create(
                name=f'Table {i}'
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created {table}')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'{table} already exists')
                )
                    
            
        self.stdout.write(self.style.SUCCESS(f'Done. {count} tables created.'))   