from django.urls import path
from .views import hello

urlspatterns = [
    path('hello/', hello),
]