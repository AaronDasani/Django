# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-11 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookReviewer', '0003_auto_20181011_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='bookReviewer.Book'),
        ),
    ]