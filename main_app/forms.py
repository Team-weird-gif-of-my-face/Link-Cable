from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Preference


class PreferenceForm(ModelForm):
    class Meta:
        model = Preference
        exclude = ['profile']

