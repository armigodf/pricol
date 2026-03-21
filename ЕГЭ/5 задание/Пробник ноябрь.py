ces = []
res = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 5 == 0 or n % 6 == 0:
        r = r + r[-1]
    else:
        r = r + (bin((n % 3) * 3)[2:])
    r = int(r, 2)
    if r <= 199:
        ces.append(r)
        res.append(n)
print(ces)



