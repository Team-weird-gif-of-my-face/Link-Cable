# Generated by Django 4.1.4 on 2022-12-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_game_name_game_game_game_system_photo_caption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite_genre',
            field=models.CharField(choices=[('A', 'Action'), ('R', 'Role-Playing'), ('S', 'Strategy'), ('D', 'Adventure'), ('I', 'Simulation'), ('C', 'Sports & Racing')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_genre',
            field=models.CharField(choices=[('A', 'Action'), ('R', 'Role-Playing'), ('S', 'Strategy'), ('D', 'Adventure'), ('I', 'Simulation'), ('C', 'Sports & Racing')], max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(choices=[('X', 'Xbox'), ('S', 'Playstation'), ('P', 'PC')], max_length=1),
        ),
    ]