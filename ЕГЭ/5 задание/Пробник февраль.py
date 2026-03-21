ces = []
res = []
for n in range(2, 1111):
    r = bin(n)[2:]
    r = r + r[1] + r[0]
    r = r[0] + r
    r = int(r, 2)
    if r > 70:
        ces.append(n)
        res.append(r)
print(min(ces))
