# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-02 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LogAndReg_app', '0002_remove_user_confirm_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]