for x in '0123456789A':
    for y in '0123456789A':
        s = int(x + '2' + y + '62', 13) + int(x + y + '138', 11)
        if s % 17 == 0:
            print(s, s // 17)