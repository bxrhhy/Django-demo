# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tips_on',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('type', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='tips',
            new_name='tips_done',
        ),
    ]