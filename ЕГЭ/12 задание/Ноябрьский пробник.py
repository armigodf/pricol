s = '6' * 39 + '2' * 44
while ("66666" in s) or ('222' in s):
    if "66666" in s:
        s = s.replace('66666', '2', 1)
    else:
        s = s.replace('222', '6', 1)
print(s)
