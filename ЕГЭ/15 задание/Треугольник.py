# def Treyg(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
#
# for A in range(1000):
#     A_ok = True
#     for x in range(10000):
#         if (not((Treyg(x, 12, 20) == (not(max(x, 11) > 10))) and Treyg(7, A, x))) == 0:
#             A_ok = False
#             break
#     if A_ok:
#         print(A)


def Treyg(a, b, c):
    return a + b > c and a + c > b and b + c > a


for A in range(1000):
    A_ok = True
    for x in range(1000):
        if ((not((Treyg(x, 11, 16)) == ((not(max(x, 5) > 10)))) and Treyg(4, A, x))) == 0:
            A_ok = False
            break
    if A_ok:
        print(A)
