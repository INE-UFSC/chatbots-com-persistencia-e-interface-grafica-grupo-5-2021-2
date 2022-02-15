from Bots.Bot import Bot
from Bots.Comando import Comando

class BotEspelhado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [
            Comando('Conte uma curiosidade', '...moc.scilobmys es-avamahC .5891 ed oçram ed 51 me odartsiger iof tenretnI ed oinìmod oriemirp O'),
            Comando('Conte uma piada', '...méugnin me anrep a assap oãn ale euqrop ,arboc A ?odnum od otsenoh siam lamina o lauQ'),
            Comando('Como ser um Bot Espelhado', '...lamron uos ue ,êcov è odahlepse è meuq mim arP')]
        self.__mensagem_de_erro = '!etsixe oan odnamoc essE'

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
        return f'...oditrevni è olaf euq odut ,odahlepsE toB o {self.__nome} uos ue ,àlO'

    def boas_vindas(self):
        return '...rednetne em agisnoc euq orepse ,uehlocse em êcoV'

    def despedida(self):
        return '...amixòrp a èta ,êcov moc rasrevnoc rezarp mu ioF'
    