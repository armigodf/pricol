import telebot
import requests
import json


bot = telebot.TeleBot('7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U')
API = "6aa13f7ea4949bf27e91510188797a94"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Дарова!!! В КАКОМ ГОРОДЕ ЖИВЁШЬ????')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'ПОГОДА СЕЙЧАС: {data["main"]["temp"]}')

        image = 'Солнце.png' if temp > 5.0 else 'сОЛНЦЕ С ТУЧЕЙ.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')


bot.polling(none_stop=True)