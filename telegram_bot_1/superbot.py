import webbrowser
from telebot import types
import telebot

bot = telebot.TeleBot('7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U')


@bot.message_handler(commands=["start"])
def start(message):
    marka = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('А ТУТ ЕСТЬ ФУЛ')
    marka.row(btn1)
    btn2 = types.InlineKeyboardButton('СНЕСТИ ЭТУ ФОТКУ')
    btn3 = types.InlineKeyboardButton('ТЕКСТ КРИНЖ, ДАВАЙ ДРУГОЙ')
    marka.row(btn2, btn3)
    file = open('./msg5318574428-88640 (1).jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=marka)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=marka)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "А ТУТ ЕСТЬ ФУЛ":
        bot.send_message(message.chat.id, "САЙТ ОТКРЫТ")
    elif message.text == "СНЕСТИ ЭТУ ФОТКУ":
        bot.send_message(message.chat.id, 'УДАЛЕНО')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'ДАРОВАААА {message.from_user.first_name}!!!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')


@bot.message_handler(commands=['site'])
def video(message):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    marka = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('А ТУТ ЕСТЬ ФУЛ', url="https://t.me/P0RNa_rt")
    marka.row(btn1)
    btn2 = types.InlineKeyboardButton('СНЕСТИ ЭТУ ФОТКУ', callback_data='delete')
    btn3 = types.InlineKeyboardButton('ТЕКСТ КРИНЖ, ДАВАЙ ДРУГОЙ', callback_data='edit')
    marka.row(btn2, btn3)
    bot.reply_to(message, 'ФОТО ТОП, А ФУЛ ЕсТЬ???', reply_markup=marka)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('ДРУГОЙ ТЕКСТ', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['mnogo'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['help'])
def not_main(message):
    bot.send_message(message.chat.id, '<b>Что ТЫ ЛЫСЫЙ,</b> <em>ПЛАКИ</em> <u>ПЛАКИ</u><b>???</b>', parse_mode='html')


# <b> = жирный шрифт; <em> = курсив; <u> = подчеркнуть текст ниже


bot.polling(none_stop=True)
