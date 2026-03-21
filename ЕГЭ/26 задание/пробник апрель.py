with open('пробник апрель.txt') as f:
    n = f.readline()
    tow = [int(i) for i in f]
    tow.sort()
    mini70 = []
    for k in range(len(tow)):
        if tow[k] <= 70:
            mini70.append(tow[k])
            tow[k] = []
    cenik = sum(mini70)
    tow = [i for i in tow if i != []]
    for j in range(len(tow) // 2):
        cenik += tow[j] * 0.63
    cenik += sum(tow[(len(tow) // 2):])
    print(cenik, tow[len(tow) // 2 - 1])
