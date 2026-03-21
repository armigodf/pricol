with open('3155.txt') as f:
    s = f.readline()
    alph = {}
    for i in range(len(s) - 1):
        if s[i] == 'A':
            key = s[i + 1]
            alph[key] = alph.get(key, 0) + 1
    print(alph) #Ответ 1567
    print(max(alph, key=alph.get))
