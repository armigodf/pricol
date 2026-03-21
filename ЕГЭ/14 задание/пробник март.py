for x in '0123':
    s = int('311' + x + '2', 4) + int('3331' + x, 4)
    if s % 98 == 0:
        print(x, s // 98)
        