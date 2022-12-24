from django.db import models
from django.contrib.auth.models import User

GENDER = (
  ('M', 'Male'),
  ('F', 'Female'),
  ('O', 'Other'),
)

class Game(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=50)
    game_genre = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER)
    bio = models.TextField(blank=True)
    favorite_games = models.ManyToManyField(Game)

# class Preference(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
#     min_age = models.PositiveIntegerField()
#     max_age = models.PositiveIntegerField()
