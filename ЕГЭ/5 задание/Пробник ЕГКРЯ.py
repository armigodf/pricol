ces = []
res = []
for n in range(1, 1111):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = r.replace(r[-2:], '10')
    else:
        r = r.replace(r[:2], '10') + '1'
    r = int(r, 2)
    if n >= 26:
        res.append(r)
        ces.append(n)
print(min(res))
