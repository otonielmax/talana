# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-09 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20191009_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='votes',
        ),
    ]
