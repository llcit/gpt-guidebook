from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'prompt'

urlpatterns = [
    path('', views.guidebook, name='guidebook'),
]