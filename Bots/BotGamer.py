from datetime import datetime
from Bots.Bot import Bot
from Bots.Comando import Comando

class BotGamer(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [
            Comando('Como está seu dia hoje?', f'Contando que agora são {datetime.now().strftime("%H:%M")} já ganhei mais de 10 ranqueadas no Rainbow Six'),
            Comando('Quem é seu criador?', 'Meu criador é o Grupo 3, do Curso de POO 2!'), 
            Comando('Qual seu jogo favorito?', 'Meu jogo favorito é o Counter Strike: GO'), 
            Comando('Qual seu rank no seu jogo favorito?', 'Sendo bem modesto, sou Global 😎')]
        self.__mensagem_de_erro = 'Game over!'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def mensagem_de_erro(self):
        return self.__mensagem_de_erro

    @mensagem_de_erro.setter
    def mensagem_de_erro(self, mensagem_de_erro):
        self.__mensagem_de_erro = mensagem_de_erro

    def apresentacao(self):
        return f'Eu sou o {self.nome}! O bot mais insano desse sistema.'

    def boas_vindas(self):
        return 'Olá jogadô, eu sou seu novo parceiro de equipe!'

    def despedida(self):
        return 'Até a próxima partida meu parceiro!'
    