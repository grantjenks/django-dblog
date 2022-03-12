import logging

from django.core.management.base import BaseCommand

dblog = logging.getLogger('dblog.' + __name__)


class Command(BaseCommand):
    help = 'Test command for dblog'

    def handle(self, *args, **options):
        dblog.info('Testing dblog in management command.')
        self.stdout.write('OK')
