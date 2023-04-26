from django.urls import path

from .views import main, login

app_name = 'telegram-login'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login, name='login'),
]
