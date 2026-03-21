f = open('sochi.txt')
vmest, n = map(int, f.readline().split())
polka = []
chem = []
for s in f:
    polka.append(int(s))
polka.sort()
for i in range(len(polka)):
    if (sum(chem) + polka[i]) <= vmest:
        chem.append(polka[i])
    elif (sum(chem[:-1]) + polka[i]) <= vmest:
        del chem[-1]
        chem.append(polka[i])
print(len(chem), max(chem))
f.close()
