from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'prompt'

urlpatterns = [
    path('generator/', views.generator, name='generator'),
    path('browser/', views.browser, name='browser'),
    path('<int:pk>/', views.detail, name='detail')
]