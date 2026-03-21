for x in ('0123456789AB'):
    s = int('2' + x + 'AF', 16) + int('8' + x + '2B', 12)
    if s % 27 == 0:
        print(x, s // 27)