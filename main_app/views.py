import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import PreferenceForm
from .models import Profile, Photo, Preference

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def connect(request):
    return render(request, 'connect.html')


@login_required
def profile_index(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  return render(request, 'profile/index.html', {'profile': profile})


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


class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['display_name', 'first_name', 'last_name', 'age', 'gender', 'bio']
  success_url = ''

  def dispatch(self, request, *args, **kwargs):
    if Profile.objects.filter(user=request.user).exists():
      return redirect('/')
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
    profile_id = self.object.id
    return f'/profile/{profile_id}/add_preference'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['display_name', 'bio']
  
  def get_success_url(self):
    profile_id = self.object.id
    return f'/profile/{profile_id}'


class PreferenceUpdate(LoginRequiredMixin, UpdateView):
  model = Preference
  fields = ['interest', 'min_age', 'max_age'] 

  def get_success_url(self):
    profile_id = self.object.profile_id
    return f'/profile/{profile_id}'


@login_required
def add_preference(request):
  error_message = ''
  if Preference.objects.filter(profile=request.user.profile).exists():
    return redirect('/')
  profile = request.user.profile
  if request.method == 'POST':
      form = PreferenceForm(request.POST)
      if form.is_valid():
        preference = form.save(commit=False)
        preference.profile = profile
        preference.save()
        return redirect('/profile/' + str(profile.id))
      else:
        error_message = 'Invalid preference - try again'
        form = PreferenceForm()
  else:
      form = PreferenceForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'profile/add_preference.html', context)


def add_photo(request, profile_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, profile_id=profile_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('/profile/' + str(profile_id), profile_id=profile_id)


# if we want to work with function based instead of class based components

# @login_required
# def create_profile(request):
#   error_message = ''
#   try:
#     request.user.profile
#     return redirect('home')
#   except Profile.DoesNotExist:
#     if request.method == 'POST':
#       form = ProfileForm(request.POST)
#       if form.is_valid():
#         profile = form.save(commit=False)
#         profile.user = request.user
#         profile.save()
#         return redirect('/profile/' + str(profile.id) + '/add_preference')
#       else:
#         error_message = 'Invalid profile - try again'
#     form = ProfileForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'profile/create_profile.html', context)


