with open('361E52.txt') as f:
    s = f.readline().replace('CD', 'C D').split()
    maxi = 0
    count = 0
    for i in range(len(s)):
        r = ''.join(s[i:i + 161])
        maxi = max(maxi, len(s))
        # print(r)
    print(maxi)
