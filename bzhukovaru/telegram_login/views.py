import asyncio

import telegram
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

def main(request):
    data = '111'
    if request.GET:
        data=request.GET.get('hash')
    if request.POST:
        data = request.POST.get('hash')+' POST'

    context = {
        'data':data,

    }
    bot = telegram.Bot(token=bot_token)
    asyncio.run(bot.send_message(124987663, data))

    return render(request, 'main.html',context)

def login(request):
    id=0
    first_name='0'
    if request.GET:
        id = request.GET.get('id')
        first_name=request.GET.get('first_name')
        last_name= request.GET.get('last_name')
        username=request.GET.get('username')
        auth_date =request.GET.get('auth_date')
        hash=request.GET.get('hash')
    if request.POST:
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        auth_date = request.POST.get('auth_date')
        hash = request.POST.get('hash')
    bot = telegram.Bot(token=bot_token)
    asyncio.run(bot.send_message(124987663, f"{id}, {first_name}"))
    print(f"{id}, {first_name}")
    return f"{id}, {first_name}"
