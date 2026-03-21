def f(s, m):
    if s >= 77 or m > 4:
        return m == 2 or m == 4
    if m % 2 == 0:
        return all([f(s + 1, m + 1), f(s + 2, m + 1), f(s * 3, m + 1)])
    return any([f(s + 1, m + 1), f(s + 2, m + 1), f(s * 3, m + 1)])


for i in range(1, 77):
    if f(i, 0):
        print(i)
