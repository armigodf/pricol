s = '2' * 50
while ('222' in s) or ('999' in s):
    if '222' in s:
        s = s.replace('222', '99', 1)
    else:
        s = s.replace('999', '2', 1)
print(s)


s = bin(192)[2:]
print(s)
