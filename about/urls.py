from .views import about, contacts
from django.urls import path, include

app_name = "about"

urlpatterns = [
    path("", about, name='about'),
    path("contacts", contacts, name='contacts')
]