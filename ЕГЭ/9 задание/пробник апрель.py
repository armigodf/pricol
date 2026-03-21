with open(r"C:\Users\davyd\OneDrive\Рабочий стол\пробник апрель.csv") as f:
    count = 0
    for line in f:
        nums = list(map(int, line.split(';')))
        nums.sort()
        pov2 = [num for num in nums if nums.count(num) == 2]
        nepov = [num for num in nums if nums.count(num) == 1]
        if len(nepov) > 0 and len(pov2) > 0:
            if ((sum(nepov) / len(nepov)) > (sum(pov2) / len(pov2))) and ((len(pov2) == 4) and (len(nepov) == 3)):
                count += 1
    print(count)
