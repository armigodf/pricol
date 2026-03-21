for A in range(128):
    A_ok = True
    for x in range(128):
        if ((x & 30 != 0) <= ((x & 16 == 0) <= (x & A != 0))) == 0:
            A_ok = False
            break
    if A_ok:
        print(A)
        