with open(r"C:\Users\davyd\Downloads\типо пробник.csv") as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        nepov = [num for num in a if a.count(num) == 1]
        if len(nepov) == 6:
            if ((a[0] + a[-1]) / 5) < (a[1] + a[2] + a[3] + a[4]) / 4:
                count += 1
    print(count)
