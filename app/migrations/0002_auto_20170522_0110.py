# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemip',
            name='ipv4',
            field=models.DecimalField(decimal_places=8, max_digits=100),
        ),
        migrations.AlterField(
            model_name='systemip',
            name='latitud',
            field=models.DecimalField(decimal_places=8, max_digits=100),
        ),
        migrations.AlterField(
            model_name='systemip',
            name='longitud',
            field=models.DecimalField(decimal_places=8, max_digits=100),
        ),
    ]
