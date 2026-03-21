with open('24 номер_9.txt') as f:
    z = f.readline().replace('PP', 'P-P')
    k = 0
    kmax = 0
    for i in z.split('-'):
        k = len(i)
        kmax = max(k, kmax)
print(kmax)
