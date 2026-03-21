num = 4 ** 644 + 4 ** 322 + 16 ** 35 - 64 ** 3
num_4 = ('')
count = 0
while num > 0:
    num_4 = str(num % 4) + num_4
    num //= 4
    c = num_4.count("3")
    count += 1
    print(count)


# alph = '012345678'  # 3 задание
# num = 81 ** 15 + 3 ** 22 - 27
# num_9 = ''
# count = 0
# while num > 0:
#     num_9 = alph[num % 9] + num_9
#     num //= 9
#     c = num_9.count("8")
#     print(c)