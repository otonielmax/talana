# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-09 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20191009_1536'),
        ('users', '0001_initial'),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
        migrations.AddField(
            model_name='pets',
            name='votes',
            field=models.ManyToManyField(to='votes.Votes'),
        ),
    ]