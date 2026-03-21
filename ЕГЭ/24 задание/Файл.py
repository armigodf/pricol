with open('Файл.txt') as f:
    s = f.readline()
    count = 2
    maxi = 0
    for i in range(0, len(s) - 2, 1):
        if s[i:i+3] == 'LDR' or s[i:i+3] == 'DRL' or s[i:i+3] == 'RLD':
            count += 1
            maxi = max(maxi, count)
        else:
            count = 2
    print(maxi)
