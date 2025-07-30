from django.urls import path
from .views import user_profiles

urlpatterns = [
    path('profiles/', user_profiles),
]
