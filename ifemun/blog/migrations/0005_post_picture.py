# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-24 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180307_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=None, upload_to=b''),
            preserve_default=False,
        ),
    ]
