import pzgram
from MQTT import *

bot = pzgram.Bot("866748587:AAG0vayDiFIEt9ictxKLoLmyfD-2YE0U2WE")
message = 'Bot Telegram che permette di visualizzare i valori rilevati dal Broker Calvino in diversi momenti: '
error_message = 'Il valore di temperatura non è stato ancora rilevato'

ist = pzgram.create_button("istantaneo", "istantaneo")
min_1 = pzgram.create_button("1 minuto", "1 minuto")
min_10 = pzgram.create_button("10 minuti", "10 minuti")
h_1 = pzgram.create_button("1 ora", "1 ora")
k = [[ist, min_1], [min_10, h_1]]
keyboard = pzgram.create_inline(k)


def start(chat):
    global message, keyboard, listaFinale
    chat.send(message, reply_markup=keyboard)


def get_istant(chat):
    global keyboard, error_message
    if not listaFinale[0]:
        chat.send(error_message)
        start(chat)
    else:
        chat.send("Il valore di temperatura istantaneo è: ".format(listaFinale[0]))
        start(chat)


def get_min1(chat):
    global keyboard, error_message
    if not listaFinale[1]:
        chat.send(error_message)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 1 minuto è: ".format(listaFinale[1]))
        start(chat)


def get_min10(chat):
    global keyboard, error_message
    if not listaFinale[2]:
        chat.send(error_message)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 10 minuti è: ".format(listaFinale[2]))
        start(chat)


def get_h1(chat):
    global keyboard, error_message
    if not listaFinale[3]:
        chat.send(error_message)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 1 ora è: ".format(listaFinale[3]))
        start(chat)


commands = {"begin": start}
bot.set_commands(commands)

queries = {"istantaneo": get_istant, "1 minuto": get_min1, "10 minuti": get_min10, "1 ora": get_h1}
bot.set_query(queries)


def main():
    bot.run()


if __name__ == '__main__':
    main()
