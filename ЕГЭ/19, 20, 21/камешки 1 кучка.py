# def f(s, m):
#     if s >= 99:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     steps = [f(s + 2, m - 1), f(s * 2, m - 1)]
#     return any(steps) if m % 2 != 0 else all(steps)
#
#
# # print('19:', [x for x in range(1, 99) if f(x, 2)])
# print('20:', [x for x in range(1, 99) if not f(x, 1) and f(x, 3)])
# print('21:', [x for x in range(1, 99) if not f(x, 2) and f(x, 4)])


# --------------------------------------------------------------------------------
# def f(s, m): 19
#     if s >= 99 or m > 2:
#         return m == 2  #РАССМАТРИВАЕМ ВАНЮ
#     return any([f(s + 2, m + 1), f(s * 2, m + 1)])
#
#
# for i in range(1, 99):
#     if f(i, 0):
#         print(i)


# def f(s, m):  20
#     if s >= 99 or m > 3:
#         return m == 3  #РАССМАТРИВАЕМ ПЕТЯ
#     if m % 2 == 1:
#         return all([f(s + 2, m + 1), f(s * 2, m + 1)])
#     return any([f(s + 2, m + 1), f(s * 2, m + 1)])
#
#
# for i in range(1, 99):
#     if f(i, 0):
#         print(i)


# def f(s, m):  21
#     if s >= 99 or m > 4:
#         return m == 2 or m == 4  #РАССМАТРИВАЕМ ВАНЯ
#     if m % 2 == 0:
#         return all([f(s + 2, m + 1), f(s * 2, m + 1)])
#     return any([f(s + 2, m + 1), f(s * 2, m + 1)])
#
#
# for i in range(1, 99):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------


# def f(s, m):
#     if s >= 172:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     steps = [f(s + 2, m - 1), f(s * 3, m - 1)]
#     return any(steps) if m % 2 != 0 else all(steps)
#
#
# # print('19:', [x for x in range(1, 172) if f(x, 2)])
# print('20:', [x for x in range(1, 172) if not f(x, 1) and f(x, 3)])
# print('21:', [x for x in range(1, 172) if not f(x, 2) and f(x, 4)])
# --------------------------------------------------------------------------------


# def f(s, m):
#     if s >= 97 or m > 2:
#         if s <= 105:
#             return m == 2
#         return m % 2 == 1
#     if m % 2 == 0:
#         return all([f(s + 3, m + 1), f(s + 5, m + 1), f(s * 3, m + 1)])
#     return any([f(s + 3, m + 1), f(s + 5, m + 1), f(s * 3, m + 1)])
#
#
# for i in range(1, 97):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------


# from math import ceil
#
#
# def f(s, m):
#     if s <= 35 or m > 2:
#         return m == 2
#     if m % 2 == 0:
#         return all([f(s - 2, m + 1), f(s - 4, m + 1), f(ceil(s / 2), m + 1)])
#     return any([f(s - 2, m + 1), f(s - 4, m + 1), f(ceil(s / 2), m + 1)])
#
#
# for i in range(36, 1111):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------


# def f(s, m):
#     if s >= 57 or m > 4:
#         return m == 2 or m == 4
#     if m % 2 == 0:
#         return all([f(s + 1, m + 1), f(s + 2, m + 1), f(s * 3, m + 1)])
#     return any([f(s + 1, m + 1), f(s + 2, m + 1), f(s * 3, m + 1)])
#
#
# for i in range(1, 57):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------


# def f(s, m):
#     if s >= 124 or m > 4:
#         return m == 2 or m == 4
#     if m % 2 == 0:
#         return all([f(s + 2, m + 1), f(s + 3, m + 1), f(s * 3, m + 1)])
#     return any([f(s + 2, m + 1), f(s + 3, m + 1), f(s * 3, m + 1)])
#
#
# for i in range(1, 124):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------


# def f(s, m):
#     if s >= 114 or m > 4:
#         return m == 2 or m == 4
#     if m % 2 == 0:
#         return all([f(s + 3, m + 1), f(s * 3, m + 1)])
#     return any([f(s + 3, m + 1), f(s * 3, m + 1)])
#
#
# for i in range(1, 114):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------

# def f(s, m):
#     if s >= 90 or m > 4:
#         return m == 2 or m == 4
#     if m % 2 == 0:
#         return all([f(s + 1, m + 1), f(s + 5, m + 1), f(s * 2, m + 1)])
#     return any([f(s + 1, m + 1), f(s + 5, m + 1), f(s * 2, m + 1)])
#
#
# for i in range(1, 41):
#     if f(i, 0):
#         print(i)
# --------------------------------------------------------------------------------


def f(s, m):
    if s >= 315 or m > 4:
        return m == 2 or m == 4
    if m % 2 == 0:
        return all([f(s + 7, m + 1), f(s * 3, m + 1), f(s * 4, m + 1)])
    return any([f(s + 7, m + 1), f(s * 3, m + 1), f(s * 4, m + 1)])


for i in range(1, 101):
    if f(i, 0):
        print(i)