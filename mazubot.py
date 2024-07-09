# -*- coding: utf-8 -*-
#Bibliotecas
from telegram import Bot
import asyncio
import schedule
import time
import logging
from aiogram import Bot

#Mensagens Automáticas
msg_1 = '🚀- Teste Amazon Prime por 1 MES de graça: https://amzn.to/3XONnME \n📖- Teste Audible Library por 3 MESES de graça: https://amzn.to/3XVozmx \n🎧- Teste Amazon Music Unlimited por 5 MESES de graça: https://amzn.to/4cNtfiw'

#Fotos automáticas
img_1 = 'https://i.pcmag.com/imagery/articles/05qp7E8Z6G2lM79Y6Epl0tl-11.jpg'

#Script
async def send_message_prime():
    bot_token = '6998561912:AAGOicoQuDHnJHY8NcLhEQKItLznmC_GrDE'
    bot = Bot(token=bot_token)
    channel_username = '@mazuofertas'

    await bot.send_photo(chat_id=channel_username, photo=img_1)
    await bot.send_message(chat_id=channel_username, text=msg_1)

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Use create_task if the loop is already running, otherwise run until complete
if loop.is_running():
    loop.create_task(send_message_prime())
else:
    loop.run_until_complete(send_message_prime())
