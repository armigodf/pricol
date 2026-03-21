with open('arfm.csv') as f:
    count = 0
    for line in f:
        num = list(map(int, line.split(';')))
        num.sort()
        pov2 = [a for a in num if num.count(a) == 2]
        nepov = [a for a in num if num.count(a) == 1]
        if len(nepov) > 0:
            if len(pov2) == 2 and len(nepov) == 4:
                if (sum(nepov) / len(nepov)) <= sum(pov2):
                    count += 1
    print(count)
