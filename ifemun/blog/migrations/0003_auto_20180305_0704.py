# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 07:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180228_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 5, 7, 3, 49, 732122, tzinfo=utc)),
        ),
    ]