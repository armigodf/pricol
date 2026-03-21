s = '3' * 10 + '1' * 240
while ('33' in s) or ('11111111' in s):
    if '33' in s:
        s = s.replace('33', '111', 1)
    else:
        s = s.replace('11111111', '5', 1)
print(s.count('5'))
