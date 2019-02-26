# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190219_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='call',
            name='early_start',
        ),
        migrations.RemoveField(
            model_name='call',
            name='late_start',
        ),
        migrations.AddField(
            model_name='call',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
    ]