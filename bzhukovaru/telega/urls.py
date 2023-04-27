from django.urls import path, include

from .views import index

app_name = 'telega'

urlpatterns = [
    path('', index, name='index'),
    ]