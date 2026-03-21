with open('20910.txt') as f:
    n, m, k = map(int, f.readline().split())
    mesta = [m] * (k + 1)
    for s in f:
        ryad, mesto = map(int, s.split())
        mesta[mesto] = min(mesta[mesto], ryad - 1)
    res = []
    for i in range(1, k):
        res.append([min(mesta[i], mesta[i + 1]), i])
        res.sort(reverse=True)
    print(res)
