# number = 0
# sub = input("Какое действие сделать? ")
# while sub != "выйти":
#     sub_list = sub.split()
#     if sub_list[0] == "добавить":
#         number += int(sub_list[1])
#     elif sub_list[0] == "убавить":
#         number -= int(sub_list[1])
#     elif sub_list[0] == "показать":
#         print(number)
#     sub = input()
#

number = 0
command = input()
while command !="выйти":
    cmd_list = command.split()
    if cmd_list[0] == "Добавить 4":
        number += int(cmd_list[1])
    if cmd_list[0] == "убавить ":
        number -= int(cmd_list[1])
    if cmd_list[0] == "показать":
        print(number)
    command = input()