with open(r"C:\Users\davyd\Downloads\9H.Y5.csv") as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        con3 = [i for i in a if abs(i) % 10 == 3 or abs(i) == 3]
        pol = [i for i in a if i > 0]
        otr = [i for i in a if i < 0]
        if (len(con3) == 3) and (sum(pol) ** 2 < sum(otr) ** 2):
            count += 1
    print(count)
