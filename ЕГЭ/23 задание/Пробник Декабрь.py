def f(x, y, z=1):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif z:
        return f(x + 2, y, z) + f(x * 2, y, 0)
    else:
        return f(x + 1, y, 1) + f(x * 2, y, 1)


print(f(1, 11, 1))
