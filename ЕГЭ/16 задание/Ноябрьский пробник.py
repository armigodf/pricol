def F(n):
    if n <= 1:
        return n
    if n > 1 and n % 2 == 0:
        return F(n - 2) + 4
    if n > 1 and n % 2 != 0:
        return F(n - 3) - 2


print(F(29) - F(27))
