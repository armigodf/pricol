def f(a, b, m):
    if a + b >= 80:
        return m % 2 == 0
    if m == 0:
        return 0
    steps = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
    return any(steps) if m % 2 != 0 else all(steps)


# print('19: ', [x for x in range(1, 79) if f(9, x, 2)])
print('20: ', [x for x in range(1, 79) if not f(9, x, 1) and f(9, x, 3)])
print('21: ', [x for x in range(1, 79) if not f(9, x, 2) and f(9, x, 4)])