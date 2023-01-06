from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('connect/', views.connect, name='connect'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('account/logout/', views.logout_index, name='logout_index'),
  path('profile_create/', views.ProfileCreate.as_view(), name='profile_create'),
  path('profile/<int:profile_id>/', views.profile_index, name='profile_index'),
  path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
  path('profile/<int:pk>/add_preference/', views.PreferenceCreate.as_view(), name='add_preference'),
  path('update_preference/<int:pk>', views.PreferenceUpdate.as_view(), name='preference_update'),
  path('profile/<int:pk>/add_game/', views.GameCreate.as_view(), name='add_game'),
  path('game/<int:game_id>/', views.game_detail, name='game_detail'),
  path('game/<int:pk>/game_update/', views.GameUpdate.as_view(), name='game_update'),
  path('game/<int:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),
  path('profile/<int:profile_id>/photo_form', views.photo_form, name='photo_form'),
  path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
  path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
  path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
  path('photo/<int:pk>/photo_update/', views.PhotoUpdate.as_view(), name='photo_update'),
  path('like/<int:profile_id>/', views.like_user, name='like_user'),
]
