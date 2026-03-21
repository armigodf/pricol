with open('24 номер_3.txt') as f:
    z = f.readline().replace('E', 'E-E')
    count = 0
    for i in z.split('-'):
        if len(i) >= 12 and i.count('E') == 2 and i.count('F') == 0:
            count += 1
    print(count)
