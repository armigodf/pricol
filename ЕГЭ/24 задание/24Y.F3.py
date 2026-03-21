with open('24Y.F3.txt') as f:
    s = f.readline().split('T')
    t = 100
    count = 0
    maxi = 0

    # Цикл для подсчета k
    for j in range(0, t + 1):
        count = count + len(s[j])
        if j != t:
            count = count + 1

    for i in range(t + 1, len(s)):
        maxi = max(maxi, count)
        count = count - len(s[i - t - 1])  # Уменьшаем k на длину элемента a[i-t-1] (исключаем старый элемент из суммы)
        count = count + len(s[i])  # Увеличиваем k на длину элемента a[i] (добавляем новый элемент в сумму)
    maxi = max(maxi, count)

    print(maxi)
