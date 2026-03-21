ces = []
res = []
for n in range(99, 10000):
    r = bin(n)[2:]
    r = r + r[0] + r[1]
    r = r[0] + r
    r = int(r, 2)
    if r > 1700:
        ces.append(n)
        res.append(r)
print(min(ces))
