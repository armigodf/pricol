with open('24 номер_6.txt') as f:
    s = f.readline()
    count = 0
    for i in s.split('A'):
        if i.count('E') >= 3:
            count = max(count, len(i))
    print(count)
