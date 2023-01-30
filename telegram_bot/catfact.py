import json

import requests
import telebot
from telebot import types

token = '5553752949:AAFTwZnmqH3TB574sjR3iLxc9iU3nRXK5kw'

bot = telebot.TeleBot(token)

def get_fact():
    url = 'https://catfact.ninja/fact/'
    response = requests.get(url).text
    return json.loads(response)['fact']


@bot.message_handler(commands=['start'])
def hello_func(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Получить факт')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку и получи факт о котах', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Получить факт')
def send_fact(message: types.Message):
    fact = get_fact()
    bot.reply_to(message, fact)


bot.polling()