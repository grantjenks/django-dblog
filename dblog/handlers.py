import logging

from django.utils import timezone


class DBLogHandler(logging.Handler):
    def emit(self, record):
        # Logging is initialized before Django apps are registered so model
        # imports must be delayed.
        from .models import Record

        kwargs = {
            'create_time': timezone.now(),
            'message': self.format(record),
            'level': record.levelno,
            'level_name': record.levelname,
            'function': record.funcName,
            'module': record.module,
            'path': record.pathname,
            'filename': record.filename,
            'line': record.lineno,
            'logger': record.name,
            'process': record.process,
            'process_name': record.processName,
            'thread': record.thread,
            'thread_name': record.threadName,
        }

        Record.objects.create(**kwargs)
