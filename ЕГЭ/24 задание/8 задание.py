with open('24 номер_8.txt') as f:
    s = f.readline()
    count = 0
    pop = 0
    maxi = 0
    for i in s:
        if i.count('A') == 1:
            maxi = max(maxi, count + pop + 1)
            pop = count
            count = 0
        else:
            count += 1
    maxi = max(maxi, count + pop + 1)
    print(maxi)

#Определите максимальное количество идущих подряд символов,
#среди которых не более одной буквы A