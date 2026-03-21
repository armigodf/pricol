with open('DDD.txt') as f:
    s = f.readline().split('K')
    min_sl = '1' * 1000
    mini = 10*6
    for x, y, z, w in zip(s, s[1:], s[2:], s[3:]):
        if (len(x) > 0) and (len(y) > 0) and (len(z) > 0) and (len(w) > 0):
            slovo = str(x + 'K' + y + 'K' + z + 'K' + w)
            if len(slovo) < mini:
                mini = len(slovo)
                min_sl = slovo
    print(mini, min_sl)
