with open('24.txt') as f:
    z = f.readline().split('G')
    count = 0
    maxi = 0
    for i in range(len(z)):
        if z[i].count('F') <= 6:
            count += len(z[i]) + 1
            maxi = max(maxi, count)
        else:
            count = 1
    print(maxi)
