s = list('РБАВЯ')
s.sort()
i = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    i += 1
                    if i == 83:
                        print(word)
