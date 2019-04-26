# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-24 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_window', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.AddField(
            model_name='player',
            name='logged_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lobby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='game_window.Lobbies'),
        ),
        migrations.AlterField(
            model_name='player',
            name='riding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='game_window.Poke_Rider'),
        ),
    ]
