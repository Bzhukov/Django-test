from django.urls import path, include

from .views import main, login

app_name = 'telegram-login'

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', main, name='main'),
    path('login/', login, name='login'),
]
