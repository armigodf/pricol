with open('kol K.txt') as f:
    s = f.readline()
    maxi = 0
    for c in f:
        if c.count('K') > maxi:
            maxi = c.count('K')
            m = [str(i) for i in c]
    al = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    kb = 0
    for i in al:
        if m.count(i) > kb:
            kb = m.count(i)
            B = i
    print(B)
