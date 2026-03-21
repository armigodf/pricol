from re import findall
with open('24 (12).txt') as f:
    s = f.readline()
    maxi = 0
    pattern = r'(?:[1-9][0-9]*)'
    a = findall(pattern, s)
    for i in a:
        if int(i) > maxi:
            maxi = int(i)
    print(maxi)
