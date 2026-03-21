def f(x, y):
    if x > y or x == 30:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 2, y) + f(x + 5, y) + f(x * 2, y)


print(f(10, 35) * f(35, 40))
