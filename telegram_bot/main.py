import telebot
from telebot import types


token = '5553752949:AAFTwZnmqH3TB574sjR3iLxc9iU3nRXK5kw'
bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton('Тыкни на меня')
keyboard.add(button)


@bot.message_handler(commands=['start', 'hi'])
def start_message(message: types.Message):
    # print(message)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Тыкни на меня')
def sticker(message: types.Message):

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHbpVj0TAniUey3gO-ao8wJNL5U7ixlQAC2xAAAnFBCEoI52tifno3dC0E')

inline_keyboard = types.InlineKeyboardMarkup()
inline_button = types.InlineKeyboardButton('Пока', callback_data='mydata')
inline_keyboard.add(inline_button)
@bot.message_handler()
def get_inline_keyboard(message: types.Message):
    bot.send_message(message.chat.id, 'Нажми на кпопку, чтобы попрощаться', reply_markup=inline_keyboard)



@bot.callback_query_handler(func=lambda callback: callback.data == 'mydata')
def goodbye(callback: types.CallbackQuery):
    bot.send_message(callback.message.chat.id, 'До свидания!')
    bot.send_sticker(callback.message.chat.id, 'CAACAgIAAxkBAAEHbuFj0TVvwArgwx77WaH2bZTZm3Y-kgACGQoAAjDB-Us-2f_QEArghC0E')
# @bot.message_handler()
# def repeat_text(message: types.Message):
#     bot.send_message(message.chat.id, message.text)


bot.polling()