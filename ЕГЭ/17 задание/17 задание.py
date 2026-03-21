s = open('17.txt')
a = [int(i) for i in s]
m = min(a)
pary = []
for g in range(1, len(a)):
    if a[g] % 12 + a[g - 1] % 12 < m:
        pary.append(a[g] + a[g - 1])
print(len(pary), max(pary))


# 17 задание