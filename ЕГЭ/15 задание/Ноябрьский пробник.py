for A in range(64):
    A_ok = True
    for x in range(64):
        if ((((x & 23) > 0) or ((x & 33) > 0)) <= ((x & A) > 0)) == 0:
            A_ok = False
            break
    if A_ok:
        print(A)
