f = open('check.txt.txt')
n = f.readline()
tow = [int(i) for i in f]
tow.sort()
mini99 = []
for k in range(len(tow)):
    if tow[k] <= 99:
        mini99.append(tow[k])
        tow[k] = []
cenik = sum(mini99)
tow = [i for i in tow if i != []]
for j in range(len(tow) // 2):
    cenik += tow[j] * 0.89
cenik += sum(tow[(len(tow) // 2):])
print(cenik, tow[len(tow) // 2 - 1])

f.close()
