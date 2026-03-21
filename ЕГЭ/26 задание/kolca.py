f = open('kolca.txt')
n = int(f.readline())
diametr = sorted([int(s) for s in f], reverse=True)
diametr_in = [diametr[0]]
for i in range(1, n):
    if diametr_in[-1] >= diametr[i] + 6:
        diametr_in.append(diametr[i])
print(len(diametr_in), min(diametr_in))
f.close()
