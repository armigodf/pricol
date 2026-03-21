white_list = set()  # Множество, в котором будет храниться "белый список"
answers = set()  # Множество будущих разрешенных ответов

white_request = 1  # Объявление переменной, через которую будут заноситься пункты белого списка
request = 1   # Объявление переменной, через которую будут заноситься пункты запросов учеников

# Работает, пока в white_request не ввели пустую строку
while white_request != '':
    white_request = input("Введите разрешёный запрос: ")
    if white_request:
        white_list.add(white_request)


# Работает, пока в request не ввели пустую строку
while request != '':
    request = input("Какой запрос? ")
    if request:
        answers.add(request)


# Перебирает множество разрешенных ответов
for answer in answers:
    if answer in white_list:
        print(answer)
