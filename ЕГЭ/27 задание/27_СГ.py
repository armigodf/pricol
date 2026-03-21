with open('27_СГ_В.txt') as f:
    n = int(f.readline())
    s = [0]
    for i in range(n):
        x, y, z = map(int, f.readline().split())
        tri = [x + y, x + z, z + y]
        combinations = [x + y for x in tri for y in s]
        s1 = [0] * 5
        for summ in combinations:
            if summ > s1[summ % 5]:
                s1[summ % 5] = summ
        s = [x for x in s1 if x != 0]
    print(max(x for x in s if x % 5 != 0))
