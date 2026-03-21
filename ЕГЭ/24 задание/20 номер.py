with open('24 номер_20.txt') as f:
    z = f.readline()
    podh = []
    alpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    pop = 0
    count = 0
    for i in range(len(z)):
        if z[i] == 'A':
            podh.append(z[i + 1])
    for j in alpha:
        if pop < podh.count(j):
            pop = podh.count(j)
            count = j
    print(count)
