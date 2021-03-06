# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-24 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_window', '0003_auto_20190424_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobbies',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdLobby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lobbies',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lobby', to='game_window.Levels'),
        ),
        migrations.AlterField(
            model_name='player',
            name='lobby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player', to='game_window.Lobbies'),
        ),
        migrations.AlterField(
            model_name='player',
            name='riding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player', to='game_window.Poke_Rider'),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logged_in_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
