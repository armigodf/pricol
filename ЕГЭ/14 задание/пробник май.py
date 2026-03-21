for x in '0123456789A':
    nums = int('4A91' + x, 11) + int('58' + x + 'A0', 11)
    if nums % 1297 == 0:
        print(x, nums // 1297)
        