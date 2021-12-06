import telebot  # импортируем библиотеку для создания бота
from telebot import types

TOKEN = '1952855741:AAGos6k3rCxBDNXAuUvIoXij3V70r2hWGYw'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hello! we are hosted on: https://dashboard.heroku.com/apps/')
    bot.send_message(message.chat.id, "We're a currency converter program. Please click below if you'd like to continue:")


bot.polling(none_stop=True)

