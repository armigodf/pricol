with open('ЗАДАНИЕ 9 ФАЙЛ 3.csv') as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        if a[0]**2 + a[1]**2 > a[2]**2:
            count += 1
    print(count)
