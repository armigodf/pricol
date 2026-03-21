with open('24 номер.txt') as f:
    s = f.readline()
    count = 0
    maxi = 0
    for x, y in zip(s, s[1:]):
        if x != y:
            count += 1
        else:
            maxi = max(maxi, count)
            count = 1
    print(maxi)
