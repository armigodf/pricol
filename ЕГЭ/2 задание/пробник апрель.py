for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (w or (y == z) or ((not(x)) and (not(y)))) == 0:
                    print(y, z, w, x)