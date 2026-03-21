s = list('КЛМН')
s.sort()
i = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        if word.count('К') == 1:
                            i += 1
print(i)
