s = '8' * 40 + '5' * 42 + '8' * 41
while ('8888' in s) or ('555' in s) or ('4444' in s):
    if '8888' in s:
        s = s.replace('8888', '888', 1)
    elif '555' in s:
        s = s.replace('555', '55', 1)
    else:
        s = s.replace('4444', '88', 1)
print(s)
