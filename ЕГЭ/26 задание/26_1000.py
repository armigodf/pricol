with open('26_1000.txt') as f:
    kol_people = int(f.readline())
    granitsa, kol_bogat, mini_bogat = 0, 1, 0
    dohod = sorted(int(x) for x in f)[::-1]
    for man in range(len(dohod) - 1):
        if kol_people / kol_bogat < 1/5:
            kol_bogat += 1
            mini_bogat = dohod[man]
            granitsa = dohod[man] - dohod[man + 1]
        elif dohod[man] - dohod[man + 1] > granitsa:
            granitsa = dohod[man] - dohod[man + 1]
            kol_bogat = man + 1
            mini_bogat = dohod[man]
    print(kol_bogat, mini_bogat)


