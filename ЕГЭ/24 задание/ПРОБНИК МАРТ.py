with open('ПРОБНИК МАРТ.txt') as f:
    s = f.readline().split('F')[1:-1]
    maxi = 0
    count = 1
    for i in range(len(s)):
        if s[i].count('Z') <= 4:
            count += len(s[i]) + 1
            maxi = max(maxi, count)
        else:
            count = 1
    print(maxi)
