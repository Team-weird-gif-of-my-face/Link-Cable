from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'first_name', 'last_name', 'age', 'gender', 'bio']