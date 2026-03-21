for A in range(0, 1000):
    A_ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((((2 * x) + (4 * y)) < A) or (x > y) or (y > 15)) == False:
                A_ok = False
                break
    if A_ok:
        print(A)
