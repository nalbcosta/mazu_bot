from tkinter import *
import bot_coding as bc

janela = Tk()
janela.title('MazuBot - Envios')
titulo = Label(janela, text='Menu')
titulo.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janela, text='Enviar Prime', command=bc.enviar_prime())
botao.grid(column=0, row=1, padx=10, pady=10)

janela.mainloop()