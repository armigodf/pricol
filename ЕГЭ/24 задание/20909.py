with open('20909.txt') as f:
    s = f.readline().replace('AB', 'A B').split()
    maxi = 0
    for i in range(len(s)):
        r = ''.join(s[i:i + 101])
        maxi = max(maxi, len(r))
    print(maxi)
 