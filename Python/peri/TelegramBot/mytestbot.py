from telebot import TeleBot,types
from time import sleep
from random import choice


TOKEN = '297133668:AAEsimushdUc1PIZXXtHMxahynWgh-idMH8'


bot = TeleBot(TOKEN)

@bot.message_handler(commands=['ucila','kadika'])
def do_something(message):
    bot.send_message(message.chat.id, 'Тестовый ответ')



@bot.message_handler(regexp='Гася')
def do_something(message):
    i = 0
    while True:
        i += 1
        bot.send_message(message.chat.id, 'Гася шлх ')
        sleep(1)

@bot.message_handler(commands=['life'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на VK", url="https://vk.com")
    keyboard.add(url_button)
    m_button = types.InlineKeyboardButton(text='Тестовая кнопка',callback_data='dead')
    keyboard.add(m_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в VK.", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def do_callback(call):
    if call.data == 'dead':
        mess = choice(['Первый вариант','второй вариант','третий вариант'])
        bot.send_message(call.message.chat.id, mess)



# @bot.message_handler(func=lambda message: True)
# def say_hello(message):
#     if message.text.lower() == 'Привет':
#         bot.send_message(message.chat.id, 'Чеза привет уцы')
#     else:
#         bot.reply_to( message, message.text + ' салам вац')


if __name__ == '__main__':
    bot.polling()
