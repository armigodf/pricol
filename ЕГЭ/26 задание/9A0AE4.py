with open('9A0AE4.txt') as f:
    n, m, k = map(int, f.readline().split())
    mesta = [m] * (k + 1)
    for a in f:
        ryad, mesto = map(int, a.split())
        mesta[mesto] = min(mesta[mesto], ryad - 1)
    res = []
    for i in range(1, k):
        res.append([min(mesta[i], mesta[i + 1]), i])
        res.sort()
    print(min(res))
