s = list('БПСТХ')
count = 0
s.sort()
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        count += 1
                        word = a + b + c + d + e + f
                        if count == 99:
                            print(word)
