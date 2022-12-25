from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def connect(request):
    return render(request, 'connect.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('create_profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



@login_required
def create_profile(request):
  error_message = ''
  try:
    request.user.profile
    return redirect('home')
  except Profile.DoesNotExist:
    if request.method == 'POST':
      form = ProfileForm(request.POST)
      if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('home')
      else:
        error_message = 'Invalid profile - try again'
    form = ProfileForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/create_profile.html', context)


# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     form = UserSignUpForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('create_profile')
#     else:
#       error_message = 'Invalid sign up - try again'
#   form = UserSignUpForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)