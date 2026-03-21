import sys
sys.setrecursionlimit(50000)


# def f(n):
#     if n == 1:
#         return 5
#     if n > 1:
#         return (2 * n) + 1 + f(n - 1)
#
#
# print(f(2024) - f(2022))


def f(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * f(n - 7)


print((f(47872) - 290 * f(47865)) / f(47858))