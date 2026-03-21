for A in range(0, 1000):
    A_ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((x <= 19) or (y < 2 * x + A - 50) or (y > 17)):
                A_ok = False
                break
    if A_ok:
        print(A)
