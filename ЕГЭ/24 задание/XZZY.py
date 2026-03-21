with open('XZZY.txt') as f:
    num = f.readline().replace('XZZY', 'XZZ_ZZY')
    count = 0
    maxi = 0
    for i in range(len(num)):
        if num[i] != '_':
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    print(maxi)
