# Импорт необходимых модулей
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import text, bold

# Подключение к базе данных SQLite
database_path = "C:/Bots/ElinaOrganics/store.db"
connection = sqlite3.connect('C:/Bots/ElinaOrganics/store.db')
cursor = connection.cursor()

# Определение путей к изображениям
photo_category = "images/test.png"
photo_faq = "images/test.png"
photo_cart = "images/cart.png"
photo_add_to_cart = "images/test.png"


# Класс конфигурации бота
class Config:
    BOT_TOKEN = "7091335689:AAFNheIPqRGNHA11U9VjB1FPZZbFGJJ-zxk"
    admin_ids = 5928342174
    SPREADSHEET_ID = '1UdqwXbEVYfmHnRGIvh1pErHBOjJFDvhuMctlsv9_IVQ'
    SERVICE_ACCOUNT_FILE = 'service-account.json'
    SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    XML_FILE_URL = 'https://bormawachs.ru/bitrix/catalog_export/yandex_161622.php'
    # Укажите путь к вашему XML-файлу здесь
