from django.urls import path
from .views import product,Vehicles
urlpatterns = [
path('check/', product),
    path('vehicle/', Vehicles)
]