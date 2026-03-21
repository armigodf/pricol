f = open('Задание 26_13.txt')
k = f.readlines()
vse = list(map(int, k))
maxisumm = 0
summa = 0
count = 0
new_csl = set(vse)
for i in range(1, len(vse) - 1):
    for j in range(i + 1, len(vse)):
        if (vse[i] + vse[j]) % 2 != 0:
            summa = vse[i] + vse[j]
            if summa in new_csl:
                count += 1
                if summa > maxisumm:
                    maxisumm = summa
print(count, maxisumm)
f.close()
