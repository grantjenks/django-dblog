import logging

from django.utils import timezone

import pytest

from .models import Record

@pytest.mark.django_db
def test_record():
    record = Record.objects.create(
        create_time=timezone.now(),
        message='This is a test.',
        level=logging.INFO,
        level_name='INFO',
        function='test_record',
        module='tests',
        path='dblog/tests.py',
        line=0,
        logger='test',
        process=123,
        process_name='Test Process',
        thread=456,
        thread_name='Test Thread',
    )
    assert str(record) == 'This is a test.'
