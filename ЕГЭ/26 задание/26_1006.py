with open('26_1006.txt') as f:
    # l, m, n = map(int, f.readline().split())
    # day = [0] * l
    # for x in range(n):
    #     start, end = map(int, f.readline().split())
    #     for j in range(start, end):
    #         day[j] += 1
    # s = ''
    # for x in day:
    #     s += str(x)
    #     prost = [x for x in s.split('1') if len(x) >= m]
    #     print(len(prost), len(max(prost)))
    l, min_pr, amount_det = map(int, f.readline().split())
    a = [0] * (l + 1)
    for i in range(amount_det):
        start, leng = map(int, f.readline().split())
        a[start] += 1
        a[leng] -= 1

    count = 0
    start1, end = 0, 0
    count1, maxi = 0, 0
    for i in range(l + 1):
        count0 = count
        count += a[i]
        if count == 0 and start1 == 0:
            start1 = i
        if (count == 1 and count0 == 0) or i == l:
            end = i
            lenght = end - start1
            if lenght >= min_pr:
                count1 += 1
                maxi = max(maxi, lenght)
            start1, end = 0, 0
        print(count1, maxi)