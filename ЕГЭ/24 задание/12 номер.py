with open('24 номер_12.txt') as f:                                     #
    z = f.readlines()
    podh = []
    maxi = 0
    alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for s in z:
        if s.count('G') <= 25:
            podh.append(s)

    for s in podh:
        for a in alph:
            maxi = max(maxi, s.rindex(a) - s.index(a))
    print(maxi)
    