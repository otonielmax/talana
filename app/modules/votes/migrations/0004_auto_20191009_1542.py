# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-09 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_votes'),
        ('pets', '0003_remove_pets_votes'),
        ('votes', '0003_auto_20191009_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='pets',
        ),
        migrations.AddField(
            model_name='votes',
            name='pets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.Pets'),
        ),
        migrations.RemoveField(
            model_name='votes',
            name='users',
        ),
        migrations.AddField(
            model_name='votes',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]
