import telebot
import requests
import os

TELEGRAM_TOKEN = '7244887422:AAHPhsodQAyQEAR5B1rc5g7mscKgNrExapk'
COZE_TOKEN = 'pat_EGPn6svSzS2pY3tW4usdSCqMRYMfvKZLLjNhNBma2FVC5gNj0FXTNIxuhk2arwub'  # подключение к ии
BOT_ID = '7386364047723741185'  # подключение к страничке ии

bot = telebot.TeleBot(TELEGRAM_TOKEN)
selected_currency_pair = ''

# Menus and keyboards
main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row('Начать торговлю на валютных парах')
main_menu.row('Получить анализ по крипте')

currency_pairs_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
currency_pairs = [
    'USD/JPY', 'GBP/USD', 'EUR/USD', 'AUD/CHF',
    'AUD/CAD', 'GBP/CAD', 'EUR/AUD', 'EUR/CHF',
    'NZD/USD', 'GBP/JPY', 'GBP/CHF', 'USD/CAD'
]
for i in range(0, len(currency_pairs), 4):
    currency_pairs_menu.row(*currency_pairs[i:i + 4])
currency_pairs_menu.row('Назад')

expiration_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
expiration_menu.row('1м', '2м', '3м')
expiration_menu.row('4м', '5м', '15м')
expiration_menu.row('Назад')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Выберите действие:", reply_markup=main_menu)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global selected_currency_pair
    chat_id = message.chat.id

    if message.text == 'Начать торговлю на валютных парах':
        bot.send_message(chat_id, 'Выберите валютную пару:', reply_markup=currency_pairs_menu)
    elif message.text == 'Получить анализ по крипте':
        bot.send_message(chat_id, 'Эта функция пока не доступна. Мы работаем над её реализацией!')
    elif message.text == 'Назад':
        bot.send_message(chat_id, 'Выберите действие:', reply_markup=main_menu)
    elif message.text in currency_pairs:
        selected_currency_pair = message.text
        bot.send_message(chat_id, f'Выбрана пара {message.text}. Выберите время экспирации:',
                         reply_markup=expiration_menu)
    elif message.text in ['1м', '2м', '3м', '4м', '5м', '15м']:
        analyze_trading(chat_id, selected_currency_pair, message.text)


def analyze_trading(chat_id, currency_pair, expiration):
    try:
        response = requests.post('https://api.coze.com/open_api/v2/chat',
                                 json={
                                     "bot_id": BOT_ID,
                                     "messages": [
                                         {
                                             "role": "user",
                                             "content": f"Проанализируй текущую ситуацию на рынке для пары "
                                                        f"{currency_pair} и дай прогноз для торговли с экспирацией "
                                                        f"{expiration}."
                                         }
                                     ]
                                 },
                                 headers={
                                     'Authorization': f'Bearer {COZE_TOKEN}',
                                     'Content-Type': 'application/json'
                                 }
                                 )
        response.raise_for_status()
        analysis = response.json()['choices'][0]['message']['content']
        bot.send_message(chat_id, f"Прогноз для {currency_pair} на {expiration}: {analysis}")
    except requests.RequestException as e:
        print(f'Error using Coze API: {e}')
        bot.send_message(chat_id, 'Произошла ошибка при получении прогноза. Попробуйте позже.')


if __name__ == "__main__":
    print('Bot setup completed, waiting for messages...')
    bot.polling(none_stop=True)
