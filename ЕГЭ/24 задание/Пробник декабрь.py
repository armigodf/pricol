with open('Файл (1).txt')as f:
    z = f.readline().replace('LDR', 'X')
    count = 0
    maxi = 0
    for i in range(len(z)):
        if z[i] == 'X':
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    print(maxi * 3)
