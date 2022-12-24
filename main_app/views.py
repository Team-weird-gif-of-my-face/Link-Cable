from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .models import Profile
from .forms import UserSignUpForm, ProfileForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def connect(request):
    return render(request, 'connect.html')

class ProfileCreate(CreateView):
  model = Profile
  fields = ['age', 'gender', 'bio', 'favorite_games']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     form = UserSignUpForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('index')
#     else:
#       error_message = 'Invalid sign up - try again'
#   form = UserSignUpForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create a new profile for the user
            profile_form = ProfileForm(request.POST)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
            return redirect('profile')
    else:
        form = UserSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})