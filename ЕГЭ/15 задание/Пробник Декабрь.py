p = list(range(10, 32))
q = list(range(13, 21))
A = list(range(1000))
for x in range(1000):
    if (((x in A) <= (x in p)) or (x in q)) == 0:
        A.remove(x)
print((A))
