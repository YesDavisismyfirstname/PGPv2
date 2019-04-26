from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Lobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('max_players', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lobby', to='game_window.Levels')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('model', models.CharField(max_length=45)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poke_Rider',
            fields=[
                ('pokemon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game_window.Pokemon')),
                ('start_pos', models.IntegerField()),
            ],
            bases=('game_window.pokemon',),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='ability',
            field=models.ManyToManyField(related_name='pokemon', to='game_window.Abilities'),
        ),
        migrations.AddField(
            model_name='player',
            name='collected',
            field=models.ManyToManyField(related_name='playerCollected', to='game_window.Pokemon'),
        ),
        migrations.AddField(
            model_name='player',
            name='lobby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='game_window.Lobbies'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logged_in_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='levels',
            name='enemy',
            field=models.ManyToManyField(related_name='level', to='game_window.Pokemon'),
        ),
        migrations.AddField(
            model_name='player',
            name='riding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='game_window.Poke_Rider'),
        ),
    ]
