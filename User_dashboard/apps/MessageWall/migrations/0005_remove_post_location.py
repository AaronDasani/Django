# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-10 04:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MessageWall', '0004_auto_20181009_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
    ]