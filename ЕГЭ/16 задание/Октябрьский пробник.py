def f(n):
    if n < 100:
        return 100
    elif n >= 100:
        return f(n - 1) + n


print(f(1000) - f(980))
