def suggestions():
    print("Предложения SkysmartBank")
    f = open("text.txt", "r", encoding="utf-8")
    text = f.read()
    print(text)
    f.close()


def complain():
    text = input("Введите вашу жалобу: ")
    f = open("complains.txt", "a", encoding="utf-8")
    f.write("\n" + text)
    f.close()
    print("Ваша жалоба будет рассмотрена в скором времени.")
