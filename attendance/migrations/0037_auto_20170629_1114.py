# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-29 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0036_auto_20170627_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='days_spend',
            new_name='hours_spend',
        ),
        migrations.AlterField(
            model_name='profile',
            name='aviable_holidays',
            field=models.FloatField(default=0),
        ),
    ]