import telebot
import random

# Токен бота (замените на свой)
TOKEN = '7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U'

# Username пользователя, которому бот отвечает (без @)
ALLOWED_USERNAME = "ArimgoCapibaraFan"  # Например: "ivan_ivanov"

# Заготовленные фразы
RESPONSES = [
    "Привет! Как дела?",
    "Отличный день, правда?",
    "Я бот, который понимает даже голосовые сообщения!",
    "Спасибо за ваше сообщение!",
    "Давайте поговорим позже.",
]

bot = telebot.TeleBot(TOKEN)


# --- Проверка пользователя ---
def is_allowed_user(message):
    username = message.from_user.username
    return username and username.lower() == ALLOWED_USERNAME.lower()


# --- Обработчик текстовых сообщений ---
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if not is_allowed_user(message):
        bot.reply_to(message, "Извините, я не могу вам ответить.")
        return

    # Реагирует на ключевые слова без "/"
    user_text = message.text.lower()

    if "привет" in user_text:
        bot.reply_to(message, "Привет! Рад вас видеть!")
    elif "как дела" in user_text:
        bot.reply_to(message, "Всё отлично, спасибо!")
    elif "пока" in user_text:
        bot.reply_to(message, "До свидания! Хорошего дня!")
    else:
        # Если нет ключевых слов — случайная фраза
        bot.reply_to(message, random.choice(RESPONSES))


# --- Запуск бота ---
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()