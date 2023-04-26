from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

def main(request):
    return render(request, 'main.html')

def login(request):
    if request.GET:
        id = request.GET.get('id')
        first_name=request.GET.get('first_name')
        last_name= request.GET.get('last_name')
        username=request.GET.get('username')
        auth_date =request.GET.get('auth_date')
        hash=request.GET.get('hash')
    return f"{id}, {first_name}"
