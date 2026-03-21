import sys
from sys import *


sys.setrecursionlimit(5000)


# def f(x, y):
#     if x > y or x == 30:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 2, y) + f(x * 3, y) + f(x * 4, y)
#
#
# print(f(5, 80) * f(80, 280))


# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
#
#
# print(f(1, 15) * f(15, 27))


# def f(x, y):
#     if x > y or x == 33:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)
#
#
# print(f(10, 30) * f(30, 40))


# def f(x, y):
#     if x > y or x == 13:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 5, y) + f(x + 7, y)
#
#
# print(f(1, 25))

#
# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 3, y) + f(x + 5, y) + f(x * 4, y)
#
#
# print(f(1, 12) * f(12, 40))


# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x + 3, y) + f(x + 5, y)
#
#
# print(f(7, 19) * f(19, 25))


# def f(x, y):
#     if x > y or x == 25:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 3, y) + f(x * 5, y) + f((x * 2) + 1, y)
#
#
# print(f(5, 95))


# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x * 2, y) + f((x * 2) + 1, y)
#
#
# print(f(3, 16) * f(16, 45))


# def f(x, y):
#     if x > y or x == 32:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 3, y) + f(x * 4, y) + f(x ** 2, y)
#
#
# print(f(12, 588))


# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 2, y) + f(x * 2, y) + f(x * 3, y)
#
#
# print(f(7, 15) * f(15, 89))


def f(x, y):
    if x < y or x == 22:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 1, y) + f(x - 4, y) + f(x / 3, y)


print(f(41, 29) * f(29, 6))