s = '3' * 106
while ('333' in s) or ('555' in s):
    if '333' in s:
        s = s.replace('333', '5', 1)
    else:
        s = s.replace('555', '33', 1)
print(s)
