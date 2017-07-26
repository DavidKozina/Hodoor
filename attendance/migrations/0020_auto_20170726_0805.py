# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-26 06:05
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0019_auto_20170223_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.CharField(max_length=20)),
                ('hours_quota', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_since', models.DateField(default=None)),
                ('date_to', models.DateField(default=None)),
                ('work_hours', models.FloatField(default=0)),
                ('verified', models.BooleanField(default=False)),
                ('reason', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aviable_holidays', models.FloatField(default=0, verbose_name='Already aviable holidays in hours')),
                ('days_of_holidays_per_year', models.IntegerField(default=20)),
                ('contracts', models.ManyToManyField(to='attendance.Contract')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='holiday',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holidays', to='attendance.Profile'),
        ),
    ]
