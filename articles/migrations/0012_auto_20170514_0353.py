# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20170514_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='submitter',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]