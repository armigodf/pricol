count = 0
for x in range(64530, 65281):
    deli = []
    for i in range(1, x + 1):
        if x % i == 0:
            deli.append(i)
    print(x, len(deli))
