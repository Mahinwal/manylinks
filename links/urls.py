from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('profile-update', views.profile_update, name='profile-update'),
    path('logout', views.user_logout, name='logout'),
    path('change-password', views.change_password, name='change-password'),
]