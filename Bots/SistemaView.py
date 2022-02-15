import PySimpleGUI as sg 

# View do padrão MVC
class SistemaView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))
        self.__bot = ''


    def tela_consulta(self):
        linha0 = [sg.Text("Escolha um bot para conversar:")]
        linha1 = [sg.Button("ordeP, o Bot Espelhado")]
        linha2 = [sg.Button("Xandão, o Bot Marombeiro")] 
        linha3 = [sg.Button("Luangameplays, o Bot Gamer")] 
        
        self.__container = [linha0, linha1, linha2, linha3]
        
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))

    def tela_bot(self, bot):
        linha0 = [sg.Text("Escolha um bot para conversar:")]
        linha1 = [sg.Button(f"{bot.comandos[0].key()}")]
        linha2 = [sg.Button(f"{bot.comandos[1].key()}")] 
        linha3 = [sg.Button(f"{bot.comandos[2].key()}")]
        linha4 = [sg.Text("", size=(40,1), key="resultado")]

        
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))


    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)


    def le_eventos(self):
        return self.__window.read()


    def fim(self):
        self.__window.close()
