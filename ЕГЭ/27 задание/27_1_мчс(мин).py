with open('27_1_мчс_А.txt') as f:
    n = int(f.readline())
    s = [0]
    for i in range(n):
        pair = list(map(int, f.readline().split()))
        combinations = [x + y for x in pair for y in s]
        s1 = [0] * 3
        for summ in combinations:
            if summ > s1[summ % 3]:
                s1[summ % 3] = summ
        s = [x for x in s1 if x != 0]
    print(max(x for x in s if x % 3 != 0))
