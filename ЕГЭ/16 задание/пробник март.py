def f(n):
    if n >= 400:
        return n
    if n < 400:
        return f(n + 1) * 3 + n


print(f(397) - f(398))
