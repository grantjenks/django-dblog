import logging
import pytest

from dblog.admin import IntPlus
from dblog.models import Record
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import Client
from django.utils import timezone

dblog = logging.getLogger('dblog.' + __name__)


@pytest.mark.django_db
def test_record():
    record = Record.objects.create(
        create_time=timezone.now(),
        message='This is a test.',
        level=logging.INFO,
        level_name='INFO',
        function='test_record',
        module='tests',
        path='tests/tests.py',
        line=0,
        logger='test',
        process=123,
        process_name='Test Process',
        thread=456,
        thread_name='Test Thread',
    )
    assert str(record) == 'This is a test.'


@pytest.mark.django_db
def test_view():
    Record.objects.all().delete()
    client = Client()
    response = client.get('/test-dblog/')
    assert response.content == b'OK'
    assert Record.objects.all().count() == 1


@pytest.mark.django_db
def test_command():
    Record.objects.all().delete()
    for count in range(10):
        dblog.info(f'Testing management command {count}')
    assert Record.objects.all().count() == 10
    call_command('cleardblog')
    assert Record.objects.all().count() == 1


@pytest.mark.django_db
def test_admin():
    User.objects.all().delete()
    dblog.info('Testing admin')
    user = User.objects.create_superuser('tester')
    client = Client()
    client.force_login(user)
    response = client.get('/admin/dblog/record/')
    assert response.status_code == 200


def test_int_plus():
    num = IntPlus(1)
    assert str(num) == '1+'
