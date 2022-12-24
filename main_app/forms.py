from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'gender', 'bio']