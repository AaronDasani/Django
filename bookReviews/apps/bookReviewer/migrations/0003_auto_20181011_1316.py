# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-11 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookReviewer', '0002_auto_20181011_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
