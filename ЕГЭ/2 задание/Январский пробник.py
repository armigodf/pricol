for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((not(x <= y)) or (y == w) or z) == 0:
                    print(w, z, y, x)
