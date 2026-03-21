with open('24 номер_7.txt') as f:
    z = f.readline()
    maxi = 0
    ind = []
    for i in range(len(z)):
        if z[i] == 'D':
            ind.append(i)
    for j in range(len(ind) - 2):
        maxi = max(maxi, ind[j + 2] - ind[j] - 1)
    print(maxi)
