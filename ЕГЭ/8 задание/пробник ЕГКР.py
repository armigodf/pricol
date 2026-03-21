s = list('СЕНТЯБРЬ')
s.sort()
i = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    i += 1
                    if (word[0] == 'Р') and (word != 'Ь') and (i % 2 == 0):
                        print(i)
