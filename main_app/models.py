from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

INTEREST = (
    ('M', 'Men'),
    ('W', 'Women'),
    ('O', 'Other'),
)

PLATFORM = (
    ('X', 'Xbox'),
    ('S', 'Playstation'),
    ('P', 'PC'),
)

GENRE = (
    ('A', 'Action'),
    ('R', 'Role-Playing'),
    ('S', 'Strategy'),
    ('D', 'Adventure'),
    ('I', 'Simulation'),
    ('C', 'Sports & Racing'),
)

class Game(models.Model):
    game = models.CharField(max_length=100)
    platform = models.CharField(
        max_length=1,
        choices=PLATFORM)
    system = models.CharField(max_length=100)
    game_genre = models.CharField(
        max_length=1,
        choices=GENRE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1,choices=GENDER)
    bio = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=1,choices=GENRE, default=GENRE[0][0])
    favorite_games = models.ManyToManyField(Game)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.id})

class Preference(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interest = models.CharField(
        max_length=1,
        choices=INTEREST)
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('preference', kwargs={'preference_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} @{self.url}"