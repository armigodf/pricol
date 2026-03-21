# from bank import *
# from client import *
# from plot import *
# import os
#
# if __name__ == "__main__":
#     global client_info
#     login = "qwerty"
#     password = "123456788"
#
#     with open("log_pass.json") as jsons:
#         defolder = json.load(jsons)
#         for i in defolder['clients']:
#             if login == i['login']:
#                 if password == i['password']:
#                     load(i['name'])
#                     break
#         else:
#             print("Неверный логин или пароль")
#     command = ""
#     while command != "10":
#         os.system('cls')
#         print("Доступные действия:")
#         print("1 - посмотреть предложения банка")
#         print("2 - отправить жалобу")
#         print("3 - информация о счетах")
#         print("4 - посмотреть прогноз доходов и расходов на следующий месяц")
#         print("5 - добавить транзакцию")
#         print("6 - посмотреть график доллара к рублю")
#         print("7 - посмотреть график доллара к йене")
#         print("10 - выйти")
#
#         command = input("Выберите действие: ")
#
#         if command == "1":
#             suggestions()
#         elif command == "2":
#             complain()
#         elif command == "3":
#             show_info()
#         elif command == "4":
#             predict()
#         elif command == "5":
#             make_transaction()
#         elif command == "6":
#             plot_rub_usd()
#         elif command == "7":
#             plot_usd_jpy()
#         elif command == "10":
#             print("Сохранение изменений...")
#             save()
#             print("адьёс")
#         else:
#             print("Действие не распознано. Попробуйте ещё раз.")
#
#         input()
#
from bank import *
from client import *
from plot import *
import os

if __name__ == "__main__":
    global client_info
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    # login = "vasya"
    # password = "12345"

    with open('log_pass.json') as json_file:
        logins = json.load(json_file)

    for el in logins["client2"]:
        if login == el['login']:
            if password == el['password']:
                load(el['name'])
                break

    else:
        print("Ошибка входа.")
        quit()

    command = ""
    while command != "10":
        os.system('cls')
        print("Доступные действия:")
        print("1 - посмотреть предложения банка")
        print("2 - отправить жалобу")
        print("3 - информация о счетах")
        print("4 - посмотреть прогноз доходов и расходов на следующий месяц")
        print("5 - добавить транзакцию")
        print("6 - посмотреть график доллара к рублю")
        print("7 - посмотреть график доллара к биткоину")
        print("10 - выйти")

        command = input("Выберите действие: ")

        if command == "1":
            suggestions()
        elif command == "2":
            complain()
        elif command == "3":
            show_info()
        elif command == "4":
            predict()
        elif command == "5":
            make_transaction()
        elif command == "6":
            plot_rub_usd()
        elif command == "7":
            plot_usd_btc()
        elif command == "10":
            print("Сохранение изменений...")
            save()
            print("До свидания.")
        else:
            print("Действие не распознано. Попробуйте ещё раз.")

        input()
