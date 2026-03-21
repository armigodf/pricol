with open('24 номер_15.txt')as f:
    z = f.readlines()
    mini = 10**10
    min_str = ''
    for i in z:
        if i.count('N') < mini:
            min_str = i
            mini = i.count('N')

    alph = {}
    for j in range(len(min_str)):
        key = min_str[j]
        alph[key] = alph.get(key, 0) + 1

    print(max(alph, key=alph.get))
