for A in range(0, 1111):
    A_ok = True
    for x in range(0, 1111):
        if (((x & 20) == 0) <= (((x & 51) != 0) <= ((x & A) != 0))) == 0:
            A_ok = False
            break
    if A_ok:
        print(A)
