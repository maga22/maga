import time
from telebot import TeleBot,types

TOKEN = '297133668:AAEsimushdUc1PIZXXtHMxahynWgh-idMH8'
bot = TeleBot(TOKEN)

@bot.message_handler(func = lambda message: True,regexp='Привет')





if __name__ == '__main__':
    bot.polling(none_stop=True)
