with open('tututu.txt') as f:
    s = f.readline().replace('TU', 'T U').split()
    maxi = 0
    for i in range(len(s)):
        r = ''.join(s[i:i + 51])
        maxi = max(maxi, len(r))
        # print(r)
    print(maxi)
