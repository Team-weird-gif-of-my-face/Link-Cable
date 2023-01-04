from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Preference, Profile
from django import forms



class PreferenceForm(ModelForm):
    class Meta:
        model = Preference
        fields = ['interest', 'age_range']

class LikeForm(ModelForm):
    class Meta:
        model = Profile
        fields =['id']
        like = forms.BooleanField(required=False)

