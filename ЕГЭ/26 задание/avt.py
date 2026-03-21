# Открываем файл для чтения
with open('avt.txt') as f:
    # Чтение количества пассажиров
    N = int(f.readline())
    events = []

    # Чтение данных о пассажирах
    for _ in range(N):
        enter, exit = map(int, f.readline().split())
        events.append((enter, 1))  # Событие входа (+1 пассажир)
        events.append((exit, -1))  # Событие выхода (-1 пассажир)

# Сортируем события по времени
events.sort()

max_passengers = 0  # Максимальное количество пассажиров
current_passengers = 0  # Текущее количество пассажиров
total_time = 0  # Общее время с хотя бы одним пассажиром
start_time = -1  # Время начала интервала с пассажирами

# Перебираем события
for time, delta in events:
    if start_time == -1:
        start_time = time  # Начинаем новый интервал
    current_passengers += delta
    if current_passengers > max_passengers:
        max_passengers = current_passengers
    if current_passengers == 0:
        # Завершаем интервал и добавляем его длину к общему времени
        total_time += time - start_time
        start_time = -1

# Вывод результата
print(max_passengers, total_time)
