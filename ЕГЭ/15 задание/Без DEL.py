# ((x <= 11) <= (x * x <= A)) and ((y * y <= A) <= (y <= 13))

# for A in range(0, 1000):
#     A_ok = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if (((x < A) <= (x ** 2 < 100)) and ((y ** 2 <= 64) <= (y <= A))) == False:
#                 A_ok = False
#                 break
#     if A_ok == True:
#         print(A)


# (y + x != 11) or (A < x) or (x < y)

# for A in range(0, 100):
#     A_ok = True
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if not ((y + x != 11) or (A < x) or (x < y)):
#                 A_ok = False
#                 break
#     if A_ok:
#         print(A)


# for A in range(0, 1000):
#     A_ok = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not (((x <= 8) <= (x * x <= A)) and ((y * y <= A) <= (y <= 15))):
#                 A_ok = False
#                 break
#     if A_ok:
#         print(A)

# count = 0
# for A in range(1, 1000):
#     A_ok = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if not (((x < 7) <= (x ** 2 < A)) and ((y ** 2 <= A) <= (y <= 9))):
#                 A_ok = False
#                 break
#     if A_ok:
#         count += 1
# print(count)


# for A in range(0, 1000):
#     A_ok = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if not ((y + 3 * x != 53) or (A < x) or(x < y)):
#                 A_ok = False
#                 break
#     if A_ok:
#         print(A)


# for A in range(0, 1000):
#     A_ok = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if (((y - 3 * x) < A) or (x > 15) or (y > 10)) == 0:
#                 A_ok = False
#                 break
#     if A_ok:
#         print(A)
#
#
# for A in range(0, 1111):
#     A_ok = True
#     for x in range(0, 1111):
#         for y in range(0, 1111):
#             if (((x & 49) == 0) <= (((x & 28) != 0) <= ((x & A) != 0)))== 0:
#                 A_ok = False
#                 break
#     if A_ok:
#         print(A)
#

for A in range(0, 1111):
    A_ok = True
    for x in range(0, 1111):
        for y in range(0, 1111):
            if (((y + 3 * x) < A) or ((y + 3) > x) or (x > 10)) == 0:
                A_ok = False
                break
    if A_ok:
        print(A)
        x