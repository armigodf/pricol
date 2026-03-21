with open('prostoi.txt') as f:
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
