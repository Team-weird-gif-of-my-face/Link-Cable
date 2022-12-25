import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile, Photo, User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def connect(request):
    return render(request, 'connect.html')

@login_required
def profile(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        return render(request, 'profile.html', {'profile': profile})
    except User.DoesNotExist:
        return redirect('create_profile')


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


# def add_photo(request, profile_id):
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         try:
#             bucket = os.environ['S3_BUCKET']
#             s3.upload_fileobj(photo_file, bucket, key)
#             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#             Photo.objects.create(url=url, profile_id=profile_id)
#         except Exception as e:
#             print('An error occurred uploading file to S3')
#             print(e)
#     return redirect('detail', profile_id=profile_id)