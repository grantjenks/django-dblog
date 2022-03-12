import logging

from django.core.management.base import BaseCommand

from dblog.models import Record

dblog = logging.getLogger('dblog.' + __name__)


class Command(BaseCommand):
    help = 'Clear dblog records'

    def handle(self, *args, **options):
        records = Record.objects.all()
        records.delete()
        dblog.info('Deleted all dblog records')
        self.stdout.write('OK')
