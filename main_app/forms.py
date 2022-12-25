from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profile


# class UserSignUpForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'first_name', 'last_name']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'first_name', 'last_name', 'age', 'gender', 'bio']