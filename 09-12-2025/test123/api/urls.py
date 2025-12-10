from django.urls import path
from .views import ok
urlpatterns = [
path('blog/', ok)
]