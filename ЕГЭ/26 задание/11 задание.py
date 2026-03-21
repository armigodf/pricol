f = open('Задание 26_11.txt')
k = f.readlines()
vse = list(map(int, k))
maxisumm = 0
summa = 0
count = 0
new_csl = set(vse)
for i in range(1, len(vse) - 1):
    for j in range(i + 1, len(vse)):
        if (vse[i] + vse[j]) % 2 == 0:
            summa = vse[i] + vse[j]
            if summa in new_csl:
                count += 1
                if summa > maxisumm:
                    maxisumm = summa
print(count, maxisumm)
f.close()

# # Чтение файла
# with open('Задание 26_11.txt') as file:
#     n = int(file.readline())
#     numbers = [int(line.strip()) for line in file.readlines()]
#
# # Подсчет пар и наибольшей суммы
# even_numbers = [number for number in numbers if number % 2 == 0]
# odd_numbers = [number for number in numbers if number % 2 == 1]
# even_sums = set()
# odd_sums = set()
# count_pairs = 0
#
# for i, number1 in enumerate(numbers):
#     for j in range(i + 1, n):
#         number2 = numbers[j]
#         if number1 % 2 == number2 % 2:
#             if number1 % 2 == 0:
#                 if number1 + number2 in even_sums:
#                     count_pairs += 1
#                 else:
#                     even_sums.add(number1 + number2)
#             else:
#                 if number1 + number2 in odd_sums:
#                     count_pairs += 1
#                 else:
#                     odd_sums.add(number1 + number2)
#
# max_sum = 0
# if even_numbers and len(even_sums) > 0:  # Если есть хотя бы одна четная сумма
#     max_sum = max(max_sum, max(even_sums))
# if odd_numbers and len(odd_sums) > 0:  # Если есть хотя бы одна нечетная сумма
#     max_sum = max(max_sum, max(odd_sums))
#
# print(count_pairs, max_sum)
