from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from movies.models import Movie

# Optional Inputs: start date, end date - if not provided, last 30 days
# Set is_valid to False for movies which their release_date is in this date range


class Command(BaseCommand):
    help = 'This is a test command and does nothing'

    def valid_date(self, value):
        try:
            return timezone.datetime.strptime(value, '%Y-%m-%d').date()
        except:
            raise CommandError(f'{value} is not a correct date')

    def add_arguments(self, parser):
        parser.add_argument('--start_date',
                            default=timezone.now().date() - timezone.timedelta(days=30),
                            type=self.valid_date)
        parser.add_argument('--end_date',
                            default=timezone.now().date(),
                            type=self.valid_date)

    def handle(self, *args, **options):
        start_date = options['start_date']
        end_date = options['end_date']

        qs = Movie.objects.filter(release_date__gte=start_date, release_date__lte=end_date)
        qs.update(is_valid=False)
        print('Done')
