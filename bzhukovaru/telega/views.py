import asyncio

import telegram
from django.conf import settings
from django.shortcuts import render


bot_token = '6062384373:AAE1v-WS0EVMvh8R9wn-BCtLIBZVgl-kTrg'



def main(request):

    bot = telegram.Bot(token=bot_token)
    asyncio.run(bot.send_message(124987663, 'main'))

    return render(request, 'main.html', )


def login(request):
    payload=None
    if request.GET.items():
        data = dict(request.GET.items())
        # hash = data.pop("hash")
        payload = "\n".join(
            sorted(["{}={}".format(k, v) for k, v in data.items()]))
    if request.POST:
        payload=request.POST
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
    if not payload:
        payload='login'
    bot = telegram.Bot(token=bot_token)
    asyncio.run(bot.send_message(124987663, payload))
    return render(request, 'main.html')
