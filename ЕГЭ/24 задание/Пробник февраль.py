with open('Пробник Февраль.txt') as f:
    s = f.readline().split('F')
    maxi = 0
    for i in range(len(s) - 1):
        maxi = max(maxi, len(s[i])+len(s[i+1])+1)
    print(maxi)
