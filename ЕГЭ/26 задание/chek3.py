f = open('check3.txt')
n = f.readline()
tow = [int(i) for i in f]
tow.sort()
cenik = 0
mini90 = []
for k in range(len(tow)):
    if tow[k] <= 90:
        mini90.append(tow[k])
        tow[k] = []
cenik = sum(mini90)
tow = [i for i in tow if i != []]
for j in range(len(tow)):
    cenik += tow[j] * 0.91
print(cenik, tow[-1] * 0.91)
