from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7312719199:AAHFOLzlqeT5cjuxn51A-dGz_y6YNR8YX1U')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    marcup = types.ReplyKeyboardMarkup()
    marcup.add(types.KeyboardButton('ОТКРЫТЬ ВЕБ СТРАНИЦУ', web_app=WebAppInfo(url='https://ggstandoff.app')))
    await message.answer('ДАРОВА', reply_markup=marcup)

executor.start_polling(dp)
