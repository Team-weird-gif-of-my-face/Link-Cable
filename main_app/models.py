from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Game(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=50)
    game_genre = models.CharField(max_length=100)

class Profile(models.Model):
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    bio = models.TextField(blank=True)
    favorite_games = models.ManyToManyField(Game)

class Preference(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()
