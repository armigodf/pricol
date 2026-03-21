for w in range(2):
    for y in range(2):
        for z in range(2):
            for x in range(2):
                if (w and (y == (z <= (x or y)))) == 1:
                    print(w, x, y, z)
