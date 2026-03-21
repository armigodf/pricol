import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
        return True


f = open('ПРОБНИК февраль.txt')
n = int(f.readline().strip())
numbers = []
for s in f:
    numbers.append(int(s))
ch_chisla = [num for num in numbers if num % 2 == 0]

max_proizv = -1
best_avg = -1
result = 0

for i in range(len(ch_chisla)):
    for j in range(i + 1, len(ch_chisla)):
        num1, num2 = ch_chisla[i], ch_chisla[j]
        avg = (num1 + num2) / 2

        num_c = min(numbers, key=lambda x: abs(x - avg))

        if is_prime(num_c):
            mult = num1 * num2
            if (mult > max_proizv) or (mult == max_proizv and avg > best_avg):
                max_proizv = mult
                best_avg = avg
                result = avg
print(result)
f.close()
