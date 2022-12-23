from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('connect/', views.connect, name='connect'),
  path('about/', views.about, name='about'),
]