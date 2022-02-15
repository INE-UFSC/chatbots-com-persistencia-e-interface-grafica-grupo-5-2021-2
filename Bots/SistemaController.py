from SistemaView import SistemaView
import PySimpleGUI as sg 
from BotEspelhado import BotEspelhado

class ClienteController:
    def __init__(self):
        self.__telaCliente = SistemaView(self)

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'ordeP, o Bot Espelhado':
                self.__telaCliente.bot = BotEspelhado

        self.__telaCliente.fim()

    def mostra_bot(self):
        self.__telaCliente.tela_bot()

        rodando = True
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            
            elif event == (f"{self.__telaCliente.bot.comandos[0].key()}"):
                self.__telaCliente.mostra_resultado(self.__telaCliente.bot.comandos[0].values())

        self.__telaCliente.fim()
