# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='issue_type',
            field=models.CharField(choices=[('B', 'Bug'), ('F', 'Feature')], default='Bug', max_length=7),
        ),
    ]
