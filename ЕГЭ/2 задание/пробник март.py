for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((not(a)) or (b and (not(d))) or (d == c)) == 0:
                    print(b, d, c, a)
