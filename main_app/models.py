from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Non-Binary'),
)

INTEREST = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Non-Binary'),
    ('E', 'Everyone')
)

PLATFORM = (
    ('X', 'Xbox'),
    ('S', 'Playstation'),
    ('P', 'PC'),
)

GENRE = (
    ('ADV', 'Adventure'),
    ('ACT', 'Action'),
    ('IND', 'Indie'),
    ('RPG', 'Role Playing Games'),
    ('SHO', 'Shooting and Combat Games'),
    ('SIM', 'Simulators'),
    ('SPO', 'Sports and Racing'),
    ('STR', 'Strategy and Puzzles')
)
FILTER = (
    ('Y', "Use Filter"),
    ('N', 'Ignore Filter')
)

class Game(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(
        max_length=1,
        choices=PLATFORM,
        default=PLATFORM[0][0])
    game_genre = models.CharField(
        max_length=3,
        choices=GENRE,
        default=GENRE[0][0])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateField('Birthday')
    gender = models.CharField(max_length=1,choices=GENDER)
    bio = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=3,choices=GENRE, default=GENRE[0][0])
    favorite_games = models.ManyToManyField(Game)
    likes = models.ManyToManyField('self',symmetrical=False, related_name='liked_by')
    matches = models.ManyToManyField('self',symmetrical=False, related_name='matched_with')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.id})


class Preference(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interest = models.CharField(
        max_length=1,
        choices=INTEREST,
        default=INTEREST[0][0]
    )
    age_range_min = models.IntegerField(validators=[MinValueValidator(18)])
    age_range_max = models.IntegerField(validators=[MinValueValidator(18)])


    def get_absolute_url(self):
        return reverse('preference', kwargs={'preference_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} @{self.url}"

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.id})