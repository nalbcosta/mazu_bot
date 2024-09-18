import bot_coding as bc
import asyncio

menu =  '''
    ----------MENU-----------
    |1 - Enviar Prime Oferta|
    |2 - Enviar Oferta      |
    |0 - Sair               |
    -------------------------
'''
print(menu)

escolha = int(input('Opção → '))

while escolha != 0:
    if escolha == 1:
        bc.enviar_prime()
        print("Mensagem de prime ofertas enviado\n")
        print(menu)
        escolha = int(input('Opção → '))
    elif escolha == 2:
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
        print(menu)
        escolha = int(input('Opção → '))
    else:
        break
