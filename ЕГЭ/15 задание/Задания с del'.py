# for A in range(0, 100):
#     A_ok = True
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if not ((y + x != 11) or (A < x) or (x < y)):
#                 A_ok = False
#                 break
#     if A_ok:
#         print(A)


# def Del(n, m):
#     if n % m == 0:
#         return 1
#     else:
#         return 0
#
#
# for A in range(1, 1000):
#     A_ok = True
#     for x in range(0, 10000):
#         if not ((not (Del(x, 26)) and Del(x, A)) <= (Del(x, 39) or not (Del(x, A)))):
#             A_ok = False
#             break
#     if A_ok:
#         print(A)


# def Del(n, m):
#     if n % m == 0:
#         return 1
#     else:
#         return 0
#
#
# for A in range(1, 1000):
#     A_ok = True
#     for x in range(0, 1000):
#         if not ((Del(x, A)) <= ((Del(x, 21)) + (Del(x, 35)))):
#             A_ok = False
#             break
#     if A_ok:
#         print(A)


# def Del(n, m):
#     if n % m == 0:
#         return 1
#     else:
#         return 0
#
#
# for A in range(1, 10000):
#     A_ok = True
#     for x in range(1, 10000):
#         if not ((not (Del(x, A))) <= (Del(x, 6) <= (not (Del(x, 4))))):
#             A_ok = False
#             break
#     if A_ok:
#         print(A)
#
#
#
# def Del(n, m):
#     return n % m
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if  ((not (Del(x, A))) <= (Del(x, 6) <= (not (Del(x, 4))))) == False:
#             break
# print(A)


# def DEL(n, m):
#     if n % m == 0:
#         return 1
#     else:
#         return 0
#
#
# for A in range(1, 1111):
#     A_ok = True
#     for x in range(1, 1111):
#         if ((not(DEL(x, A))) <= (DEL(x, 8) <= (not(DEL(x, 5))))) == False:
#             A_ok = False
#             break
#     if A_ok:
#         print(A)


# def Del(n, m):
#     if n % m == 0:
#         return 1
#     else:
#         return 0
#
#
# for A in range(1, 1111):
#     A_ok = True
#     for x in range(1, 1111):
#         if ((A < 81) and ((not(Del(x, A))) <= (Del(x, 9) <= (not(Del(x, 27)))))) == False:
#             A_ok = False
#             break
#     if A_ok:
#         print(A)
