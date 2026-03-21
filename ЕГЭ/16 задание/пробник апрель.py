def f(n):
    if n >= 230:
        return n
    if n < 230:
        return f(n + 1) - n


print(f(230) - f(225))
