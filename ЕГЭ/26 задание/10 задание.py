f = open('Задание 26_10.txt')

n = int(f.readline())
mesta = [[] for i in range(10000+1)]
fr_mesta = []

for i in range(n):
    ryad, mesto = map(int, f.readline().split())
    mesta[ryad].append(mesto)
for j in range(len(mesta)):
    if len(mesta) >= 2:
        mesta[j].sort()
    for k in range(len(mesta[j]) - 1):
        if mesta[j][k + 1] - mesta[j][k] == 3:
            fr_mesta.append((j, mesta[j][k] + 1))
print(max(fr_mesta))
f.close()
