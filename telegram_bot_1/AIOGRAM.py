from aiogram import Bot, dispatcher, executor, types

bot = Bot('7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U')
dp = dispatcher(bot)


@dp.message.hendler()  # commands=['start']
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    await message.reply('Hello')



executor.start_polling(dp)
