# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-10 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MessageWall', '0003_post_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='LoginAndRegister.User'),
        ),
    ]
