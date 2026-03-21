ces = []
res = []
for n in range(1, 111):
    r = bin(n)[2:]
    if str(r).count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if str(r).count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    r = int(r, 2)
    if r > 46:
        res.append(r)
        ces.append(n)
print(min(res))
