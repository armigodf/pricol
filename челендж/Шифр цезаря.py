eng = "abcdefghijklmnopqrstuvwxyz"
rus = "абвгдеёжзийклмнопрстуфхцчщъыьэюя"
cipher = input("Что шифровать будем ")
scor = ""
for i in cipher:
    if i.lower() in eng:
        scor += eng([eng.index(i.lower)+13])
    elif i.lower() in rus:
        scor += rus[(rus.index(i.lower)+13)]
    else:
        print("Другой язык ")
print(scor)
