with open('9.24.csv') as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        pov = [i for i in a if a.count(i) == 3]
        nepov = [i for i in a if a.count(i) == 1]
        if len(nepov) == 4:
            sr_nepov = sum(nepov) / 4
            sr_pov = sum(pov) / 3
            if sr_nepov <= sr_pov:
                count += 1
    print(count)
