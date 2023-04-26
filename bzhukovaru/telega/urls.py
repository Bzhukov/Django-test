from django.urls import path

from .views import main, login

app_name = 'telega'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login, name='login'),
    ]