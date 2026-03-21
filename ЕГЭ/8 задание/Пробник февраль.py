s = list('ЛAЙПЮ')
s.sort()
i = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        i += 1
                        if i == 793:
                            print(word)