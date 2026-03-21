for a in range(2):
    for b in range(2):
        for d in range(2):
            for g in range(2):
                if (((b <= a) and (d or b)) <= ((g and not(a)) or b)) == 0:
                    print(g, b, d, a)
