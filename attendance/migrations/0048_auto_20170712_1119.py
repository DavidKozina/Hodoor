# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-12 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0047_auto_20170712_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_action_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]