f = open('mag.txt')
n = f.readline()
tow = [int(i) for i in f]
tow.sort()
cenik = 0
mini76 = []
for k in range(len(tow)):
    if tow[k] <= 76:
        mini76.append(tow[k])
        tow[k] = []
cenik = sum(mini76)
tow = [i for i in tow if i != []]
for j in range(len(tow) // 2):
    cenik += tow[j] * 0.69
cenik += sum(tow[(len(tow) // 2):])
print(cenik, tow[len(tow) // 2 - 1])

f.close()
