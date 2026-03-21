s = '2' * 3 + '6' * 50
while ('26' in s) or ('2' in s):
    if '26' in s:
        s = s.replace('26', '662', 1)
    else:
        s = s.replace('2', '66', 1)
print(s.count('6'))
