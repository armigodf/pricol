for x in '0123456789AB':
    z = int(x + 'B' + '65', 12) + int('A' + x + 'A' + '4', 12)
    if z % 21 == 0:
        z //= 21
        print(z)
