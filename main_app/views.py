import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import PreferenceForm, LikeForm
from .models import Profile, Photo, Preference, Game
from django.db.models import Q
import datetime


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def connect(request):

  try:
    user_profile = Profile.objects.get(user=request.user)
    preference = Preference.objects.get(profile=user_profile)
    interest = preference.interest
    min_age = preference.age_range_min
    max_age = preference.age_range_max

    # filter profiles by favorite genre and interest
    filtered_profiles = Profile.objects.exclude(user=request.user).filter(
        Q(favorite_genre=user_profile.favorite_genre) & Q(gender=interest)
    )

    # filter by age range
    filtered_profiles = filtered_profiles.filter(
        birthday__gte=datetime.date(year=datetime.datetime.now().year - max_age, month=1, day=1),
        birthday__lte=datetime.date(year=datetime.datetime.now().year - min_age, month=1, day=1)
    )

    return render(request, 'connect.html', {'filtered_profiles': filtered_profiles})

  except Preference.DoesNotExist:
    profile = request.user.profile
    return redirect('/profile/' + str(profile.id) + '/add_preference')



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
      return redirect('profile_create')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def logout_index(request):
  return render(request, 'registration/logout.html')

class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['display_name', 'first_name', 'last_name', 'birthday', 'gender', 'bio', 'favorite_genre','contact_info']
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
  fields = ['display_name', 'bio', 'favorite_genre', 'contact_info']
  success_url = ''
  
  def get_success_url(self):
    profile_id = self.object.id
    return f'/profile/{profile_id}'

class PreferenceCreate(LoginRequiredMixin, CreateView):
  model = Preference
  fields = ['interest', 'age_range_min','age_range_max']
  success_url=''

  def dispatch(self, request, *args, **kwargs):
    if Preference.objects.filter(profile=request.user.profile).exists():
      return redirect('/')
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.profile_id = self.request.user.profile.id
    return super().form_valid(form)

  def get_success_url(self):
    profile_id = self.object.profile_id
    return f'/profile/{profile_id}'


class PreferenceUpdate(LoginRequiredMixin, UpdateView):
  model = Preference
  form_class = PreferenceForm

  def get_success_url(self):
    profile_id = self.object.profile_id
    return f'/profile/{profile_id}'

@login_required
def photo_form(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  return render(request, 'profile/upload_photo.html', {'profile': profile})


def add_photo(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    if profile.photo_set.exists():
        profile.photo_set.first().delete()

    photo_file = request.FILES.get('photo-file', None)
    caption = request.POST.get('caption', '')
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, caption=caption, profile=profile)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('/profile/' + str(profile_id), profile_id=profile_id)



def photo_detail(request, photo_id):
  photo = Photo.objects.get(id=photo_id)
  return render(request, 'profile/photo_detail.html', {'photo': photo})

class PhotoUpdate(UpdateView):
  model = Photo
  fields = ['caption']

  def get_success_url(self):
    photo_id = self.object.id
    return f'/photo/{photo_id}'


class PhotoDelete(LoginRequiredMixin, DeleteView):
  model = Photo
  success_url = ''
  
  def get_success_url(self):
    profile_id = self.object.profile_id
    return f'/profile/{profile_id}'
    

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'platform', 'game_genre']

  def form_valid(self, form):
      game = form.save(commit=False)
      game.save()

      profile = self.request.user.profile

      profile.favorite_games.add(game)
      profile.save()

      self.success_url = reverse('profile_index', kwargs={'profile_id': profile.id})
      return super().form_valid(form)


def game_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'profile/game_detail.html', {'game': game})


class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['platform'] 

  def get_success_url(self):
    game_id = self.object.id
    return f'/game/{game_id}'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = ''
  
  def get_success_url(self):
    profile_id = self.request.user.profile.id
    return f'/profile/{profile_id}'

def create_match(user1, user2):
  if user1 in user2.likes.all() and user2 in user1.likes.all():
    user1.matches.add(user2)
    user2.matches.add(user1)
    user1.save()
    user2.save()
    return (user1, user2)
  else:
    return None

def like_user(request, profile_id):
  liked_user = get_object_or_404(Profile, pk=profile_id)
  current_user = request.user.profile
  if request.method == 'POST':
    form = LikeForm(request.POST)
    current_user.likes.add(liked_user)
    current_user.save()
    match = create_match(current_user, liked_user)
    if match is not None:
      messages.success(request, 'You have a new match!')
    else:
      messages.success(request, 'User liked')
    return redirect('connect')
  else:
    form = LikeForm()
  return render(request, 'index.html', {'form':form, 'user':liked_user})
