with open('ЗАДАНИЕ 9 ФАЙЛ 2.csv') as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        if a[0] * a[1] + a[0] * a[2] < a[1] * a[2]:
            count += 1
    print(count)
