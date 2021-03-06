# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-19 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20170819_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='difficulty_level',
        ),
        migrations.AddField(
            model_name='building',
            name='q_skipped',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='q_solved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='q_total',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='building',
            name='q_wrong',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='difficulty_level',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(default='0000000000000000000000000', max_length=40),
        ),
    ]
