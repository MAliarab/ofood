# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20171026_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='saatKari',
            field=models.CharField(max_length=40),
        ),
    ]
