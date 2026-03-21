with open('Задание 26_9.txt') as f:
    n, m = map(int, f.readline().split())
    f = [i.split() for i in f]
    f = sorted([[int(i[0]), i[1]]for i in f])
    a = []
    b = []
    for i in range(len(f)):
        if (sum(a + b) + f[i][0]) <= m:
            if f[i][1] == 'A':
                a.append(f[i][0])
                f[i] = []
            elif f[i][1] == 'B':
                b.append(f[i][0])
                f[i] = []
    f = [i for i in f if i != []]
    for i in f:
        if i[1] == 'A':
            if sum(a + b) - b[-1] + i[0] <= m:
                a.append(i[0])
                b.pop(-1)
    print(len(a), m - sum(a + b))
