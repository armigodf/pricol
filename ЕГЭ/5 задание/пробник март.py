ces = []
res = []
for n in range(1, 1111):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '100' + r
    else:
        r = '10' + r + '001'
    r = int(r, 2)
    if r > 500:
        ces.append(n)
        res.append(r)
print(min(ces))
