import telebot

bot = telebot.TeleBot('345454484:AAGS8ewILZCOIwZkKoFo4cZHBtTHBDBtJoo')
upd = bot.get_updates()
last_upd = upd[-1]
message_from_user = last_upd.message
@bot.message_handler(content_types='text')
def send_mes(message):
    bot.send_message(message.chat.id,'Тест')


bot.polling(none_stop=True)
