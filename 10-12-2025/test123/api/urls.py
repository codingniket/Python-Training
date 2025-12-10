from django.urls import path
from .views import employees
urlpatterns = [
path('employees/', employees),
path('employees/<int:id>/', employees),
# path('blog/welcome', welcome),
# path('blog/status', status),
# path('dele', dele),
# path('d/',view_person),
]