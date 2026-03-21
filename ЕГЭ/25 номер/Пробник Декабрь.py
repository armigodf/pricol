count = 0
for x in range(65106, 65149):
    deli = []
    for i in range(2, x):
        if x % i == 0:
            deli.append(i)
    if len(deli) == 6:
        count += 1
print(count)