import sys
sys.setrecursionlimit(1050)


def f(n):
    if n == 1:
        return n
    if n > 1:
        return 2 * n + f(n - 1)


print(f(1040) - f(1037))
