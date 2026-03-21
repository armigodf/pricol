with open('пробник май.txt') as f:
    num = f.readline().replace('ABC', 'AB_BC').split('_')
    maxi = 0
    for i in range(len(num)):
        if len(num[i]) > maxi:
            maxi = len(num[i])
    print(maxi)