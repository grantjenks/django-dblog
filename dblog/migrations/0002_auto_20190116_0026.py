# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-16 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='level',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='line',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='process',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='thread',
            field=models.BigIntegerField(),
        ),
    ]
