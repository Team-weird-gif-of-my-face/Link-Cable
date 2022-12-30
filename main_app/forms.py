from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Preference

class PreferenceForm(ModelForm):
    class Meta:
        model = Preference
        fields = ['interest', 'age_range']