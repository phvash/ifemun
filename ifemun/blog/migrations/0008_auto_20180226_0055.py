# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 00:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180219_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 26, 0, 55, 18, 112723, tzinfo=utc)),
        ),
    ]