def f(x, y):
    if x > y or x == 95:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)


print(f(80, 92) * f(92, 120))
