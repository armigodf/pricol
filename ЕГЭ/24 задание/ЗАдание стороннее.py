with open('24 (1).txt') as f:
    s = f.readline()
    pop = 0
    posl = []
    for i in s:
        if not (i in posl):  # Максимальная длина непрерывной
            posl.append(i)   # последовательности из уникальных символов
        else:
            if len(posl) > pop:
                pop = len(posl)
            posl = [i]
print(pop)
