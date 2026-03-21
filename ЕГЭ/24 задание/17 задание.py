with open('24 номер_17.txt') as f:
    z = f.readline()
    rzn = []
    pop = 0
    count = 0
    alfpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(len(z) - 2):
        if z[i] == z[i + 1]:
            rzn.append(z[i + 2])
    for j in alfpha:
        if pop < rzn.count(j):
            pop = rzn.count(j)
            count = j
    print(count)
