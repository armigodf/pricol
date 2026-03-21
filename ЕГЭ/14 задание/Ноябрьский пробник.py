for x in '01234':
    for y in '01234':
        z = int('187' + y + x, 20) + int('2' + x + '2' + y, 5)
        if z % 20 == 0:
            print(x, y, z // 20)
