# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 13:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default=datetime.datetime(2016, 3, 10, 13, 37, 9, 762567, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
