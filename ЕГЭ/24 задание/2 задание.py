with open('24 номер_2 (1).txt') as f:
    z = f.readline().replace('A', 'A-A')
    count = 0
    for i in z.split('-'):
        if len(i) >= 10 and i.count('B') == 0 and i[0] == i[-1] == 'A' and i.count('A') == 2:
            count += 1
    print(count)
