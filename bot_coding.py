import os
import requests
import asyncio
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
from telegram import Bot

#Mensagens Automáticas
msg_1 = '🚀- Teste Amazon Prime por 1 MES de graça: https://amzn.to/3XONnME \n📖- Teste Audible Library por 3 MESES de graça: https://amzn.to/3XVozmx \n🎧- Teste Amazon Music Unlimited por 5 MESES de graça: https://amzn.to/4cNtfiw'

#Fotos automáticas
img_1 = 'https://i.pcmag.com/imagery/articles/05qp7E8Z6G2lM79Y6Epl0tl-11.jpg'


load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

async def enviar_oferta(e):
    bot = Bot(token=bot_token)
    channel_username = '@mazuofertas'
    await bot.send_message(chat_id=channel_username, text=e)
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

def extrair_informacoes_oferta(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = bs(response.content, 'html.parser')

        nome_produto_element = soup.find('span', {'id': 'productTitle'})
        preco_produto_element = soup.find('span', {'class': 'a-price-whole'})

        foto_produto_element = soup.find('img', {'id': 'landingImage'})
        if foto_produto_element:
            imagem_url = foto_produto_element.get('src')
        else:
            imagem_url = None
        
        if nome_produto_element:
            nome_produto = nome_produto_element.get_text().strip()
        else:
            nome_produto = 'Nome do produto não encontrado'
        
        if preco_produto_element:
            preco_produto = preco_produto_element.get_text().strip()
        else:
            preco_produto = 'Preço do produto não encontrado'
        
        mensagem_formatada = f'🚩{nome_produto}\n💥Preço de oferta: R${preco_produto}00💥\n📦 {url}'

        if imagem_url:
            mensagem_formatada += f"\n📷 Imagem do produto: {imagem_url}"

        mensagem_formatada += "\n⚠️ Preços sujeitos à alteração sem prévio aviso."
        mensagem_formatada += "\n🚛 Seja assinante prime e obtenha frete grátis para produtos enviados pela Amazon: https://amzn.to/3XONnME"

        return mensagem_formatada

    except Exception as e:
        print(f'Erro ao fornecer as informações da oferta{e}')
        return None

async def enviar_prime():
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
    loop.create_task(enviar_prime())
else:
    loop.run_until_complete(enviar_prime())