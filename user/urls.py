from django.urls import path
from .views import login, profile, registration, logout_view

app_name = 'user'

urlpatterns = [
    path("", login, name='login'),
    path("registration/", registration, name='registration'),
    path("profile/", profile, name='profile'),
    path("logout/", logout_view, name="logout")
]

