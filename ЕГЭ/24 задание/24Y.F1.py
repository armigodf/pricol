with open('24Y.F1.txt') as f:
    z = f.readline().replace('AB', '#').replace('CB', '#')
    count = 0
    maxi = 0
    for i in range(len(z)):
        if z[i] == '#':
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    print(maxi)
