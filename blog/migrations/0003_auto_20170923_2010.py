# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 16:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170923_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 23, 16, 39, 47, 932202, tzinfo=utc)),
        ),
    ]
