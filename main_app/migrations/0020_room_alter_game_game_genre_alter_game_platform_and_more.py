# Generated by Django 4.1.4 on 2023-01-02 20:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0019_alter_game_game_genre_alter_game_platform_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='game_genre',
            field=models.CharField(choices=[('ADV', 'Adventure'), ('ACT', 'Action'), ('IND', 'Indie'), ('RPG', 'Role Playing Games'), ('SHO', 'Shooting and Combat Games'), ('SIM', 'Simulators'), ('SPO', 'Sports and Racing'), ('STR', 'Strategy and Puzzles')], default='ADV', max_length=3),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(choices=[('X', 'Xbox'), ('S', 'Playstation'), ('P', 'PC')], default='X', max_length=1),
        ),
        migrations.AlterField(
            model_name='preference',
            name='age_range',
            field=models.CharField(choices=[('R1', '18-24'), ('R2', '25-34'), ('R3', '35-44'), ('R4', '45-54'), ('R5', '55+')], max_length=2),
        ),
        migrations.AlterField(
            model_name='preference',
            name='interest',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('T', 'Trans'), ('A', 'All')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_genre',
            field=models.CharField(choices=[('ADV', 'Adventure'), ('ACT', 'Action'), ('IND', 'Indie'), ('RPG', 'Role Playing Games'), ('SHO', 'Shooting and Combat Games'), ('SIM', 'Simulators'), ('SPO', 'Sports and Racing'), ('STR', 'Strategy and Puzzles')], default='ADV', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('N', 'Non-Binary'), ('P', 'Prefer not to say')], max_length=1),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('room', models.ManyToManyField(to='main_app.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]