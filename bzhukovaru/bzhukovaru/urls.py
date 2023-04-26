from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from social_django.views import auth, complete

urlpatterns = [
    path('', include('telegram_login.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
