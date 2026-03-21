with open("2_9.csv") as f:
    count = 0
    for line in f:
        s = list(map(int, line.split(';')))
        s.sort()
        if (s[0] + s[-1]) ** 2 > s[1] ** 2 + s[2] ** 2 + s[3] ** 2:
            count += 1
    print(count)
    