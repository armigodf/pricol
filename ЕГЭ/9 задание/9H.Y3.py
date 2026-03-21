with open(r'/9H.Y3.csv') as f:
    count = 0
    for line in f:
        a = list(map(int, line.split(';')))
        a.sort()
        pov3 = [i for i in a if a.count(i) == 3]
        pov2 = [i for i in a if a.count(i) == 2]
        nepov = [i for i in a if a.count(i) == 1]
        if (len(pov3) == 3 and len(pov2) == 2 and len(nepov) == 3) and (pov3[0] > pov2[0]):
            count += 1
    print(count)