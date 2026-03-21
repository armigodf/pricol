with open('урочный.csv') as f:
    count = 0
    for line in f:
        num = list(map(int, line.split(',')))
        num.sort()
        pov = [i for i in num if num.count(i) > 1]
        nepov = [i for i in num if num.count(i) == 1]
        if len(nepov) == 0:
            nepov.append(0)
        if len(set(pov)) == 2:
            if sum(set(pov)) < sum(nepov):
                count += 1
    print(count)
