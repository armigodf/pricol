with open('прикол.csv') as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        nepov = [i for i in a if a.count(i) == 1]
        if len(nepov) > 0 and len(nepov) == 5:
            if ((nepov[-1] + nepov[0]) / 2) > ((nepov[1] + nepov[2] + nepov[3]) / 3):
                count += 1
    print(count)
