# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_tips_on_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips_on',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tips_done',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
