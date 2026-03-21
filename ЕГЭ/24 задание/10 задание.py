with open('24 номер_10.txt') as f:
    z = f.readline().replace('ad', 'a-d').replace('da', 'd-a')
    k = 0
    kmax = 0
    for i in z.split('-'):
        k = len(i)
        kmax = max(k, kmax)
print(kmax)