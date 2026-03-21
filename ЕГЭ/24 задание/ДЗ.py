with open('ДЗ1.txt') as f:
    z = f.readline().replace('PP', 'P_P')
    count = 0
    maxi = 0
    for i in z.split('_'):
        count = len(i)
        maxi = max(count, maxi)
print(maxi)
