with open('24 номер_1.txt') as f:
    z = f.readline().replace('CA', '#').replace('DA', '#').replace('FA', '#').replace('CO', '#').replace('DO', '#').replace('FO', '#')
    count = 0
    maxi = 0
    for i in range(len(z)):
        if z[i] == '#':
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    print(maxi)

