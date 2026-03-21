s = list('ФАПШЮ')
s.sort()
i = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            word = a + b + c + d + e + f + g
                            i += 1
                            if i == 586:
                                print(word)
