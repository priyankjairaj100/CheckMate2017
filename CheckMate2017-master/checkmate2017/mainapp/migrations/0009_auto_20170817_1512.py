# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_gameswitch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameswitch',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
