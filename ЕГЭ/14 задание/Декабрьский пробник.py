for x in '0123456789ABDEF':
    z = int('123' + x + '5', 16) + int('1' + x + '233', 16)
    if z % 12 == 0:
        print(z, z // 12)
