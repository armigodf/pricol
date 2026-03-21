with open('hghghg.txt') as f:
    s = f.readline().replace('HJ', 'H J').split()
    maxi = 0
    count = 0
    for i in range(len(s)):
        r = ''.join(s[i:i + 361])
        maxi = max(maxi, len(r))
        # print(r)
    print(maxi)