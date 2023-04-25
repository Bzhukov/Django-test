from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from social_django.views import auth, complete

urlpatterns = [
    path('', include('telegram_login.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('auth/', auth, name='social_auth'),
    path('auth/complete/', complete, name='social_complete'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
