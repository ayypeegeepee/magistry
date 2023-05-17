import telebot
import numpy as np
from telebot import TeleBot
import onnxruntime as ort
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from PIL import Image
import time

bot = telebot.TeleBot('6099651839:AAE4HNqR8yy5C6ZhAUWvNfwcdrqQJrE2fRQ')
model_path = "model/model.onnx"
imageClassList = {'0': 'Барокко', '1': 'Брутализм', '2': 'Классицизм', '3': 'Конструктивизм', '4': 'Ампир',
                  '5': 'Экспрессионизм', '6': 'Готический стиль', '7': 'Пуук (Стиль Майя)'}
wiki_articles = {'Барокко': 'https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D0%BE%D0%BA%D0%BA%D0%BE',
                 'Брутализм': 'https://ru.wikipedia.org/wiki/%D0%91%D1%80%D1%83%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%BC',
                 'Классицизм': 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%86%D0%B8%D0%B7%D0%BC',
                 'Конструктивизм': 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%B8%D0%B2%D0%B8%D0%B7%D0%BC_(%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%BE)',
                 'Ампир': 'https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%BF%D0%B8%D1%80',
                 'Экспрессионизм': 'https://ru.wikipedia.org/wiki/%D0%AD%D0%BA%D1%81%D0%BF%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%BE%D0%BD%D0%B8%D0%B7%D0%BC',
                 'Готический стиль': 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%82%D0%B8%D0%BA%D0%B0',
                 'Пуук (Стиль Майя)': 'https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%83%D0%BA'}


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 'Привет! Я бот для определения самых популярных архитектурных стилей! Просто загрузи сюда сжатую картинку и я постараюсь её определить. '
                 'Ты можешь посмотреть список моих команд написав /help!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
                 'Это список моих команд: \n/help - показать список команд \n/echo - повторить твое сообщение!'
                 '\n/chat_id - узнать ID этого чата (для отладки) \n/secret - не советую даже пробовать')


@bot.message_handler(commands=['echo'])
def echo(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['chat_id'])
def handle_all_messages(message):
    bot.send_message(text=f'ID - {message.chat.id}', chat_id=message.chat.id)


@bot.message_handler(commands=['secret'])
def test(message):
    bot.send_message(message.chat.id, "Ты точно этого хочешь?", reply_markup=start_keyboard)


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# start_keyboard.add(KeyboardButton(">Одуматься и очистить чат"), KeyboardButton(">Настаивать на своем"))
start_keyboard.add(KeyboardButton(">Настаивать на своем"))


# Обработчик первой кнопки
@bot.message_handler(func=lambda message: message.text == '>Настаивать на своем')
def press_button(message):
    bot.send_message(message.chat.id, "Ты прям уверен что хочешь?", reply_markup=menu_keyboard)


menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# menu_keyboard.add(KeyboardButton("Да"), KeyboardButton("Нет"))
menu_keyboard.add(KeyboardButton("Одумайся пока не поздно. Очисти чат"))
last_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
last_keyboard.add(KeyboardButton("Ну я предупреждал....."))


# Обработчик кнопки "Кнопка 1"
@bot.message_handler(func=lambda message: message.text == 'Одумайся пока не поздно. Очисти чат')
def process_btn1(message):
    bot.send_message(message.chat.id, 'Ну я предупреждал.....')
    send_gif(message)


#
# # Обработчик кнопки "Кнопка 2"
# @bot.message_handler(func=lambda message: message.text == 'Нет')
# def process_btn2(message):
#     clear_chat(message)


def send_gif(message):
    chat_id = message.chat.id
    gif_path = "secret/secret.gif"
    with open(gif_path, 'rb') as gif:
        bot.send_document(chat_id, gif)


def clear_chat(message):
    message_id = message.message_id
    chat_id = message.chat.id
    messages = bot.get_updates()
    for update in messages:
        if update.message.chat.id == chat_id:
            try:
                bot.delete_message(chat_id, update.message.message_id)
            except:
                pass
    bot.send_message(chat_id, "История сообщений в чате успешно очищена")


@bot.message_handler(content_types=['photo'])
def photo(message):
    photo_info = bot.get_file(message.photo[-1].file_id)
    photo_file = bot.download_file(photo_info.file_path)
    with open(f'Photo_from_tg_bot.jpg', 'wb') as file:
        file.write(photo_file)
    img = Image.open('Photo_from_tg_bot.jpg').convert("RGB")
    img = np.asarray(img.resize((224, 224), Image.ANTIALIAS))
    sess = ort.InferenceSession(
        r'model\model.onnx')
    outputOFModel = np.argmax(sess.run(None, {'input': np.asarray([img]).astype(np.float32)}))
    score = imageClassList[str(outputOFModel)]

    bot.reply_to(message, f'Скорее всего это {score}')
    bot.send_message(text=f'Думаю Вам будет интересно почитать про него {wiki_articles[score]}',
                     chat_id=1387200899)


if __name__ == '__main__':
    bot.polling(none_stop=True)
