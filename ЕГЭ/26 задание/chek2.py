f = open('check2 .txt')
n = f.readline()
tow = [int(i) for i in f]
tow.sort()
cenik = 0
mini150 = []
for k in range(len(tow)):
    if tow[k] <= 150:
        mini150.append(tow[k])
        tow[k] = []
cenik = sum(mini150)
tow = [i for i in tow if i != []]
for j in range(len(tow)):
    cenik += tow[j] * 0.80
print(cenik, tow[-5] * 0.80)

f.close()
