# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-09 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_votes'),
        ('pets', '0003_remove_pets_votes'),
        ('votes', '0002_auto_20191009_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='date_vote',
        ),
        migrations.AddField(
            model_name='votes',
            name='pets',
            field=models.ManyToManyField(to='pets.Pets'),
        ),
        migrations.AddField(
            model_name='votes',
            name='users',
            field=models.ManyToManyField(to='users.Users'),
        ),
    ]