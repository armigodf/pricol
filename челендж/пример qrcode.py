# import qrcode
#
# data = 'you are amazing'
#
# # Следующие две строчки для быстрого создания QR-кода.
# # img = qrcode.make(data)
# # img.save('test.png')
#
# # Эти строчки для более тонкой настройки QR-кода
# qr = qrcode.QRCode(
#     version=5,      # Версия qr-кода. Принимает числа от 1 до 40
#     box_size=15,    # Размер изображения с qr-кодом. Чем больше число, тем больше картинка
#     border=10       # Толщина границы, отделяющая qr-код от края изображения
# )
# qr.add_data(data)   # Шифрует информацию
# img = qr.make_image(fill_color='chocolate', back_color='moccasin')  # Настраивает внешний вид qr-кода. Можно использовать любые системные имена цветов
# img.save('test.png')    # Сохраняет изображение в файл. Если указываете только имя файла, обращайте внимание на путь, прописанный в терминале - файл появится именно там.
#
from челендж import qrcode

# Введите данные, которые вы хотите закодировать
data = "https://www.example.com"

# Создайте объект QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Добавьте данные в QR-код
qr.add_data(data)
qr.make(fit=True)

# Создайте изображение QR-кода
img = qr.make_image(fill_color="black", back_color="white")

# Сохраните изображение QR-кода в файл
img.save("qrcode.png")
