import bot_coding as bc
import asyncio


url_oferta = str(input('Informe a URL da oferta: '))
mensagem_oferta = bc.extrair_informacoes_oferta(url_oferta)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

if mensagem_oferta:
    bc.enviar_oferta(mensagem_oferta)
    if loop.is_running():
        loop.create_task(bc.enviar_oferta(mensagem_oferta))
    else:
        loop.run_until_complete(bc.enviar_oferta(mensagem_oferta))
else:
    print('Não foi possivel enviar as informações da oferta')

