from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('telegram_login.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
