import sys
sys.setrecursionlimit(3500)
from decimal import Decimal, getcontext
getcontext().prec = 1000000

# def f(n):
#     if n < 3000:
#         return n
#     if n >= 3000:
#         return 2 * (n + 2) * f(n - 1)
#
#
# print((f(3002) - 2 * f(3000))/f(2998))


# def f(n):
#     if n < 200:
#         return 7
#     if n >= 200:
#         return n * f(n - 1) * 2
#
#
# print((f(1022) - f(1021)) / f(1020))


# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * n * f(n - 1)
#
#
# print((f(2024) - f(2023)) / f(2022))

# _______________________________________________________________
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return Decimal(n) * f(n - 1)
#
#
# print((f(2024)/Decimal(4) + f(2023)) / f(2022))


# def factorial(n):
#     res = Decimal(1)
#     for i in range(2, n + 1):
#         res *= Decimal(i)
#     return res
#
#
# f2022 = factorial(2022)
# f2023 = f2022 * Decimal(2023)
# f2024 = f2023 * Decimal(2024)
#
# print(((f2024) / Decimal(4) + f2023) / f2022)
# ________________________________________________________________


def f(n):
    if n <= 3000:
        return n
    if n > 3000:
        return 2 * n - 5 + f(n - 1)


print(f(3001) - f(2098))