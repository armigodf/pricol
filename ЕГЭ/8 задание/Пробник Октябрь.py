a = {0: 'Д', 1: 'И', 2: 'К', 3: 'М', 4: 'Щ'}
k = 0
for i in range(0, len(a)):
    for g in range(0, len(a)):
        for f in range(0, len(a)):
            for d in range(0, len(a)):
                for s in range(0, len(a)):
                    for h in range(0, len(a)):
                        k += 1
                        if k == 324:
                            print(a[i], a[g], a[f], a[d], a[s], a[h], end=' ')
