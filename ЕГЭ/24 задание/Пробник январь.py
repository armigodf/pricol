with open('Задание 24.txt') as f:
    s = f.readline()
    count = 1
    maxi = 0
    for i in range(len(s) - 1):
        if s[i] == 'D' and s[i + 1] == 'D':
            count += 1
            maxi = max(maxi, count)
        else:
            count = 1
    print(maxi)
