# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20170629_1638'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tips_on',
            new_name='tips',
        ),
        migrations.DeleteModel(
            name='tips_done',
        ),
    ]
