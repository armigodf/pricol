ces = []
res = []
for n in range(1, 1111):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '000'
    if n % 2 != 0:
        r = r + '11'
    r = int(r, 2)
    if r < 50:
        ces.append(n)
        res.append(r)
print(max(ces))
