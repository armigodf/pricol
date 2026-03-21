for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((not(x)) and z) or (w and x) or y) == 0:
                    print(z, y, x, w)
