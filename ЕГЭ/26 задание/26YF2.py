with open('26YF2.txt') as f:
    n = int(f.readline())
    izmenenie = [0] * 1440
    for i in range(n):
        start, end = [int(x) for x in f.readline().split()]
        izmenenie[start] += 1
        izmenenie[end] -= 1

    in_shop = 0
    maxi = -1
    for minuta in range(1440):
        in_shop += izmenenie[minuta]
        maxi = max(maxi, in_shop)
    print(maxi)

    in_shop = 0
    count_peak = 0
    for minuta in range(1440):
        in_shop += izmenenie[minuta]
        if in_shop == maxi and izmenenie[minuta] != 0:
            count_peak += 1
    print(count_peak)
