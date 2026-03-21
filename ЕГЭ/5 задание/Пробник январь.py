ces = []
res = []
for n in range(1, 11111):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '10' + r + '11'
    r = int(r, 2)
    if r > 2024:
        ces.append(n)
        res.append(r)
print(ces)
