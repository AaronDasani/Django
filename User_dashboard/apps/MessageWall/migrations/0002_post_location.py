# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-06 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageWall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
