from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('connect/', views.connect, name='connect'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('create_profile/', views.create_profile, name='create_profile'),
  # path('profile/', views.profile, name='profile'),
]