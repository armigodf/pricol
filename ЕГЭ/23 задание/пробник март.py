def f(x, y):
    if x > y or x == 8 or x == 28:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)


print(f(5, 26) * f(26, 30))
