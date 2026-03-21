with open('24 номер_18.txt') as f:
    z = f.readline()
    rzn = []
    pop = 0
    count = 0
    alfpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(len(z) - 2):
        if z[i] == z[i + 2]:
            rzn.append(z[i + 1])
    for j in alfpha:
        if pop < rzn.count(j):
            pop = rzn.count(j)
            count = j
    print(count)
