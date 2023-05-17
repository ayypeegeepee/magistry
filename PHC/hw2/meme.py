import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6099651839:AAE4HNqR8yy5C6ZhAUWvNfwcdrqQJrE2fRQ')


@bot.message_handler(commands=['secret'])
def test(message):
    bot.send_message(message.chat.id, "Ты точно этого хочешь?", reply_markup=start_keyboard)


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(KeyboardButton(">Одуматься и очистить чат"), KeyboardButton(">Настаивать на своем"))


# Обработчик первой кнопки
@bot.message_handler(func=lambda message: message.text == '>Настаивать на своем')
def press_button(message):
    bot.send_message(message.chat.id, "Ты прям уверен что хочешь?", reply_markup=menu_keyboard)


menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Да"), KeyboardButton("Нет"))


# Обработчик кнопки "Кнопка 1"
@bot.message_handler(func=lambda message: message.text == 'Да')
def process_btn1(message):
    bot.send_message(message.chat.id, 'Вы нажали на кнопку 1')


# Обработчик кнопки "Кнопка 2"
@bot.message_handler(func=lambda message: message.text == 'Нет')
def process_btn2(message):
    bot.send_message(message.chat.id, 'Вы нажали на кнопку 2')


@bot.message_handler(commands=['secret'])
def send_gif(message):
    chat_id = message.chat.id
    gif_path = "secret/secret.gif"
    with open(gif_path, 'rb') as gif:
        bot.send_document(chat_id, gif)


@bot.callback_query_handler(func=lambda call: call.data == '>Одуматься и очистить чат')
def clear_chat(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    # очистка чата
    bot.delete_message(chat_id, message_id)
    messages = bot.history(chat_id=chat_id)
    for message in messages:
        bot.delete_message(chat_id, message.message_id)