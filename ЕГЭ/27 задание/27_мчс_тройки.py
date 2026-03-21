with open('27_мчс_тройки B.txt') as f:
    n = int(f.readline())
    s = [0]
    for i in range(n):
        chet = list(map(int, f.readline().split()))
        combinations = [x + y for x in chet for y in s]
        s1 = [0] * 4
        for summ in combinations:
            if summ > s1[summ % 4]:
                s1[summ % 4] = summ
        s = [x for x in s1 if x != 0]
    print(max(x for x in s if x % 4 != 0))
