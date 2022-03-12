import logging

from django.http import HttpResponse

dblog = logging.getLogger('dblog.' + __name__)


def test_dblog(request):
    dblog.info('Testing dblog in view.')
    return HttpResponse('OK', content_type='text/plain')
