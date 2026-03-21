ces = []
res = []
for n in range(1, 1111):
    r = bin(n)[2:]
    r = r + str(r.count('1') % 2)
    r = r + str(r.count('1') % 2)
    r = r + '0'
    r = int(r, 2)
    if r > 120:
        ces.append(n)
        res.append(r)
print(min(res))
