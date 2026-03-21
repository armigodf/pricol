def f(a, b, m):
    if a + b >= 129 or m > 4:
        return m == 2 or m == 4
    if m % 2 == 0:
        return all([f(a+2, b, m+1), f(a, b+2, m+1), f(a+5, b, m+1), f(a, b+5, m+1), f(a*2, b, m+1), f(a, b*2, m+1)])
    return any([f(a+2, b, m+1), f(a, b+2, m+1), f(a+5, b, m+1), f(a, b+5, m+1), f(a*2, b, m+1), f(a, b*2, m+1)])


for i in range(1, 129):
    if f(10, i, 0):
        print(i)
