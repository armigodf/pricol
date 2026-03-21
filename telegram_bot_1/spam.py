# import logging
# import re
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import ParseMode
#
# # Вставьте сюда ваш токен бота
# API_TOKEN = '7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U'
#
# # Настройка логирования
# logging.basicConfig(level=logging.INFO)
#
# # Инициализация бота и диспетчера
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['spam'])
# async def mention_all(message: types.Message):
#     if message.chat.type != 'supergroup':
#         await message.reply('Эта команда доступна только в супергруппах.')
#         return
#
#     members = await bot.get_chat_administrators(message.chat.id)
#     mention_text = ""
#
#     for member in members:
#         user = member.user
#         mention_text += f"[{user.first_name}](tg://user?id={user.id}) "
#
#     if len(mention_text) > 0:
#         await bot.send_message(chat_id=message.chat.id, text=mention_text, parse_mode=ParseMode.MARKDOWN)
#     else:
#         await message.reply("Не удалось получить список участников.")
#
#
# if __name__ == '__main':
#     executor.start_polling(dp, skip_updates=True)


# import asyncio
# from aiogram import Bot, Dispatcher, types
#
# API_TOKEN = '7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U'
#
# # Инициализируем бота и диспетчера
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# # Обработка команды /start
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.reply("Привет! Я бот, который будет отмечать всех участников чата.")
#
#
# # Обработка всех входящих сообщений
# @dp.message_handler(commands=['spam'])
# async def echo(message: types.Message):
#     await message.reply(f"@{message.from_user.username} - участник чата.")
#     return
#
# # Запуск бота
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.create_task(dp.start_polling())
#     loop.run_forever()


import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U'  # заменить на свой API токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Список участников
participants = ["@ChristmasGLHF", '@EuSentoGabu', '@ArimgoCapibaraFan']


@dp.message_handler(commands=['spam'])
async def start(message: types.Message):
    for participant in participants:
        await message.answer(f'{participant} отмечен.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
