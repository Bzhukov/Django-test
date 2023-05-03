from django.urls import path, include

from .views import index,auth

app_name = 'telega'

urlpatterns = [
    path('', index, name='index'),
    path('222/', auth, name='index'),
    ]