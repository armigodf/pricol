with open('korziki.txt') as f:
    n = int(f.readline())
    diametr = sorted([int(s) for s in f], reverse=True)
    diametr_in = [diametr[0]]
    for i in range(1, n):
        if diametr_in[-1] >= diametr[i] + 3:
            diametr_in.append(diametr[i])
    print(len(diametr_in), min(diametr_in))
