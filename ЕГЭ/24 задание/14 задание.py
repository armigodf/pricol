with open('24 номер_14.txt') as f:
    s = f.readlines()
    maxi = 0
    alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for i in s:
        if i.count('A') < 25:
            for j in alph:
                maxi = max(maxi, i.rindex(j) - i.index(j))
    print(maxi)
#В строках, содержащих менее 25 букв A,
#нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.