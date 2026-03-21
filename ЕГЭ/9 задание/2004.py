with open(r"C:\Users\davyd\OneDrive\Рабочий стол\2004.csv") as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        if (a[0] != a[1] != a[2] != a[3] != a[4]) and (((a[0] + a[-1]) / 2) > ((a[1] + a[2] + a[3]) / 3)):
            count += 1
    print(count)
