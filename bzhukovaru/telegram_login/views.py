import asyncio

import telegram
from django.conf import settings
from django.shortcuts import render

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL


def main(request):

    bot = telegram.Bot(token=bot_token)
    asyncio.run(bot.send_message(124987663, 'main'))

    return render(request, 'main.html', )


def login(request):
    data = dict(request.GET.items())
    hash = data.pop("hash")
    payload = "\n".join(
        sorted(["{}={}".format(k, v) for k, v in data.items()]))
    # if request.GET:
    #     data = request.GET.items()
    #     id = request.GET.get('id')
    #     first_name = request.GET.get('first_name')
    #     last_name = request.GET.get('last_name')
    #     username = request.GET.get('username')
    #     auth_date = request.GET.get('auth_date')
    #     hash = request.GET.get('hash')
    # if request.POST:
    #     id = request.POST.get('id')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     username = request.POST.get('username')
    #     auth_date = request.POST.get('auth_date')
    #     hash = request.POST.get('hash')
    bot = telegram.Bot(token=bot_token)
    asyncio.run(bot.send_message(124987663, f'{hash} {payload}'))
    return render(request, 'main.html')
