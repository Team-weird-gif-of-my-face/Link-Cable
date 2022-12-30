from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('connect/', views.connect, name='connect'),
  path('connect/search', views.connect_view, name='connect_view'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('create_profile/', views.ProfileCreate.as_view(), name='profile_create'),
  path('profile/<int:profile_id>/', views.profile_index, name='profile_index'),
  path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
  path('profile/<int:pk>/add_preference/', views.PreferenceCreate.as_view(), name='add_preference'),
  path('update_preference/<int:pk>', views.PreferenceUpdate.as_view(), name='preference_update'),
  path('profile/<int:pk>/add_game/', views.GameCreate.as_view(), name='add_game'),
  path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
  path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
  path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
  path('photo/<int:pk>/photo_update/', views.PhotoUpdate.as_view(), name='photo_update'),
]
# if we want to work with function based instead of class based components
  # path('create_profile/', views.create_profile, name='create_profile'),
  # path('profile/<int:profile_id>/add_preference/', views.add_preference, name='add_preference'),