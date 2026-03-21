def f(a, b, m):
    if a + b >= 67:
        return m % 2 == 0
    if m == 0:
        return 0
    steps = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a * 4, b, m - 1), f(a, b * 4, m - 1)]
    return any(steps) if m % 2 != 0 else all(steps)


# print('19: ', [x for x in range(1, 61) if f(5, x, 2)])
print('20: ', [x for x in range(1, 61) if not f(5, x, 1) and f(5, x, 3)])
print('21: ', [x for x in range(1, 61) if not f(5, x, 2) and f(5, x, 4)])
