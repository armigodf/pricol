with open('24 номер_19.txt') as f:
    z = f.readline()
    podh = []
    alfpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    pop = 0
    count = 0
    for i in range(len(z)):
        if z[i] == 'E':
            podh.append(z[i + 1])
    for j in alfpha:
        if pop < podh.count(j):
            pop = podh.count(j)
            count = j
    print(count)
