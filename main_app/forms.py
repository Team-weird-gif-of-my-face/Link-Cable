from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Preference

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'first_name', 'last_name', 'age', 'gender', 'bio']

class PreferenceForm(ModelForm):
    class Meta:
        model = Preference
        fields = ['gender', 'min_age', 'max_age']