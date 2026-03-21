with open('символы.txt') as f:
    s = f.readline().replace('of', 'o_f').replace('fo', 'f_o').split('_')
    maxi = 0
    for i in range(len(s)):
        maxi = max(maxi, len(s[i]))
    print(maxi)
