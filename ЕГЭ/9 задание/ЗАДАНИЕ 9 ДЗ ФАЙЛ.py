with open('Задание 9 ДЗ ФАЙЛ.csv') as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        print(a)
        if a[0] * a[2] + a[0] * a[1] > a[1] * a[2]:
            count += 1
    print(count)
