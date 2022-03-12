"""Django Database Logs Models
"""

from django.db import models


class Record(models.Model):
    create_time = models.DateTimeField()
    message = models.TextField()
    level = models.BigIntegerField()
    level_name = models.CharField(max_length=16)
    function = models.CharField(max_length=80)
    module = models.CharField(max_length=80)
    path = models.CharField(max_length=260)
    filename = models.CharField(max_length=80)
    line = models.BigIntegerField()
    logger = models.CharField(max_length=80)
    process = models.BigIntegerField()
    process_name = models.CharField(max_length=80)
    thread = models.BigIntegerField()
    thread_name = models.CharField(max_length=80)

    def __str__(self):
        return self.message
