s = list('РПЯА')
s.sort()
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                cnt += 1
                if cnt == 30:
                    print(word)
