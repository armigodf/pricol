with open('3157.txt') as f:
    s = f.readline()
    alph = {}
    for i in range(len(s) - 2):
        if s[i] == 'X' and s[i + 2] == 'Z':
            key = s[i + 1]
            alph[key] = alph.get(key, 0) + 1
    print(alph)
    print(max(alph, key=alph.get))
