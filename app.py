#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotEspelhado import BotEspelhado
from Bots.BotGamer import BotGamer
from Bots.BotMarombeiro import BotMarombeiro

###construa a lista de bots disponíveis aqui
lista_bots = [BotEspelhado("ordeP"), BotMarombeiro("Xandão"), BotGamer("Luangameplays")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
