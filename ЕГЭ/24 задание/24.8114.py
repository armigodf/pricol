from re import findall
with open('24.8114.txt') as f:
    s = f.readline()
    maxi = 0
    pattern = r'(?:[1-9ABCD][0-9ABCD]*)'
    res = findall(pattern, s)
    for i in res:
        if int(i, 14) % 98 == 0:
            maxi = max(maxi, len(i))
    print(maxi)
