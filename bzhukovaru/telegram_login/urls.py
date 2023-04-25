from django.urls import path

from .views import main

app_name = 'telegram-login'

urlpatterns = [
    path('', main, name='main'),
]
