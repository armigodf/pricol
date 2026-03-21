# def f(a, b, m):
#     if a + b >= 160:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     steps = [f(a + 2, b, m - 1), f(a, b + 2, m - 1), f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
#     return any(steps) if m % 2 != 0 else all(steps)
#
#
# # print('19: ', [x for x in range(1, 61) if f(20, x, 2)])
# print('20: ', [x for x in range(1, 140) if not f(20, x, 1) and f(20, x, 3)])
# print('21: ', [x for x in range(1, 140) if not f(20, x, 2) and f(20, x, 4)])


# def f(a, b, m):  19
#     if a + b >= 160 or m > 2:
#         return m == 2  #РАССМАТРИВАЕМ ВАНЮ
#     return any([f(a+2,b,m+1), f(a+3,b,m+1), f(a*2,b,m+1), f(a,b+2,m+1), f(a,b+3,m+1), f(a,b*2,m+1)])
#
#
# for i in range(1, 140):
#     if f(20, i,  0):
#         print(i)


# def f(a, b, m):  20
#     if a + b >= 160 or m > 3:
#         return m == 3  #РАССМАТРИВАЕМ ПЕТЮ
#     if m % 2 == 1:
#         return all([f(a + 2, b, m + 1), f(a + 3, b, m + 1), f(a * 2, b, m + 1), f(a, b + 2, m + 1), f(a, b + 3, m + 1),
#                     f(a, b * 2, m + 1)])
#     return any([f(a+2,b,m+1), f(a+3,b,m+1), f(a*2,b,m+1), f(a,b+2,m+1), f(a,b+3,m+1), f(a,b*2,m+1)])
#
#
# for i in range(1, 140):
#     if f(20, i,  0):
#         print(i)


# def f(a, b, m):  21
#     if a + b >= 160 or m > 4:
#         return m == 2 or m == 4  #РАССМАТРИВАЕМ ВАНЮ
#     if m % 2 == 0:
#         return all([f(a + 2, b, m + 1), f(a + 3, b, m + 1), f(a * 2, b, m + 1), f(a, b + 2, m + 1), f(a, b + 3, m + 1),
#                     f(a, b * 2, m + 1)])
#     return any([f(a+2,b,m+1), f(a+3,b,m+1), f(a*2,b,m+1), f(a,b+2,m+1), f(a,b+3,m+1), f(a,b*2,m+1)])
#
#
# for i in range(1, 140):
#     if f(20, i,  0):
#         print(i)
# --------------------------------------------------------------------------------


# def f(a, b, s):
#     if a + b >= 41 or s > 4:
#         return s == 2 or s == 4
#     if s % 2 == 0:
#         return all([f(a+1,b+2,s+1), f(a+2,b+1,s+1), f(a*2,b,s+1),f(a,b*2,s+1)])
#     return any([f(a+1,b+2,s+1), f(a+2,b+1,s+1), f(a*2,b,s+1),f(a,b*2,s+1)])
#
#
# for i in range(1, 33):
#     if f(8, i, 0):
#         print(i)
# --------------------------------------------------------------------------------


# def f(a, b, m):
#     if a + b >= 58 or m > 4:
#         return m == 2 or m == 4
#     if m % 2 == 1:
#         return all([f(a+4,b,m+1),f(a,b+4,m+1),f(a*4,b,m+1),f(a,b*2,m+1)])
#     return any([f(a+4,b,m+1),f(a,b+4,m+1),f(a*4,b,m+1),f(a,b*2,m+1)])
#
#
# for i in range(1, 46):
#     if f(i, 12, 0):
#         print(i)
# --------------------------------------------------------------------------------


