from django.urls import path
from .views import suggest_path

urlpatterns = [
    path('suggest-path/', suggest_path, name='suggest_path'),
]
