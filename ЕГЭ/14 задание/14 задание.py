# result_search = []
# for x in '01234567':
#     for y in '01234567':
#         z = int(x + '43' + y + '2', 8) + int('7' + x + y + '21', 13)
#         if z % 33 == 0:
#             result_search.append(z)
# if result_search:
#     print(min(result_search) // 33)


# for x in '0123456789ABCDEFGHI':    # 19-ичная система счисления
#     num = int("98897" + x + '21', 19) + int('2' + x + '923', 19)
#     if num % 18 == 0:
#         print(x, num // 18) #ОТВЕТ: F 469034148


# for x in '0123456789ABCDE':
#     num = int('9897' + x + '21', 15) + int('12' + x + '023', 15)
#     if num % 14 == 0:
#         print(x, num // 14) #ОТВЕТ: 6 7853726


# for x in '0123456789ABC':
#     for y in '0123456789ABC':
#         num = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
#         if num % 9 == 0:
#             print(x, y, num // 9)


# for x in '0123456789AB':  # 1 Задание
#     for y in '0123456789AB':
#         num = int(x + '201' + y, 12) + int('1' + x + '195' + y, 19)
#         if num % 170 == 0:
#             print(x, y, num // 170)
#
#
# alph = '0123456'  # 2 задание
# num = 7 ** 2684 + 2401 ** 1316 + 339
# num_7 = ''
# count = 0
# while num > 0:
#     num_7 = alph[num % 7] + num_7
#     num //= 7
#     c = num_7.count("6")
#     print(c)


# alph = '012345678'  # 3 задание
# num = 81 ** 15 + 3 ** 22 - 27
# num_9 = ''
# count = 0
# while num > 0:
#     num_9 = alph[num % 9] + num_9
#     num //= 9
#     c = num_9.count("8")
#     print(c)


# for x in '0123456789AB':  # 4 задание
#     for y in '0123456789AB':
#         num = int(y + 'AA' + x, 12) + int(x + '02' + y, 14)
#         if num % 80 == 0:
#             print(x, y, num // 80)


# for x in '0123456789A':   # 5 задание
#     num = int('95' + x + '2', 11) + int(x + '458', 12)
#     if num % 136 == 0:
#         print(x, num // 136)


# for x in range(2030, 0, -1):
#     num = 7 ** 170 + 7 ** 100 - x
#     count = 0
#     while num > 0:
#         if num % 7 == 0:
#             count += 1
#             num //= 7
#     if num == 71:
#         print(x, count)
#         break


# for x in range(2030, 0, -1):
#     alph = '0123456'
#     num = 7 ** 170 + 7 ** 100 - x
#     count = 0
#     num_7 = ''
#     while num > 0:
#         num_7 = alph[num % 7] + num_7
#         num //= 7
#         if num_7.count('0') == 71:
#             print(x) #ОТВЕТ: 2029


# alph = '0123456789ABCDEFGHIJKLMNO'   # 25 система счисления
# num = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2025
# num_25 = ''
# count = 0
# while num > 0:
#     num_25 = alph[num % 25] + num_25
#     if (num % 25) == 0:
#         count += 1
#     num //= 25
# print(num_25)
# print(count)


# alph = '01234'
# num = 125 ** 3576 + 5 ** 1615 - 129
# num_5 = ''
# count = 0
# while num > 0:
#     num_5 = alph[num % 5] + num_5
#     num //= 5
#     c = num_5.count("4")
#     print(c)


# for x in '0123456789ABCDE':
#     num = int(x + 'A8E', 15) + int(x + '645', 15)
#     if num % 77 == 0:
#         print(x, num // 77)


# for x in '0123456789A':
#     num = int('21' + x + '17', 11) + int('2' + x + '160', 11)
#     if num % 10 == 0:
#         print(num, num // 10)


# num = 2**1165 + 16**2383 - 8
# num_2 = bin(num)[2:]
# num_2 = ''
# count = 0
# while num > 0:
#     num_2 = str(num % 2) + num_2
#     num //= 2
# print(num_2.count('1'))


# num = 27**2886 + 9**1815 - 3**3933 - 10
# num_3 = ''
# while num > 0:
#     num_3 = str(num % 3) + num_3
#     num //= 3
# print(num_3.count('2'))


# num = 343**3978 + 2401**1560 + 7**2739 - 49
# num_7 = ''
# while num > 0:
#     num_7 = str(num % 7) + num_7
#     num //= 7
# print(num_7.count('0'))


# for x in '01234567':
#     num = int('123' + x, 8) + int('7' + x + '27', 8)
#     if num % 542 == 0:
#         print(x, num // 542)


# for x in '0123456789ABCDEF':
#     num = int('FB71' + x, 16) + int(x + '8E74', 16)
#     if num % 1229 == 0:
#         print(x, num // 1229)


# num = 16807**35 + 2401**2 * 343**9 - 49**52 + 7**3 - 2005
# num49 = ''
# alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm'
# count = 0
# while num > 0:
#     num49 = alphabet[num % 49] + num49
#     if num % 49 > 9:
#         count += 1
#     num //= 49
# print(count)


# num = 5 * 729**2024 + 3 * 243**1413 - 7 * 81**169 - 2 * 9**107 + 3017
# num27 = ''
# summ = 0
# alph = '0123456789ABCDEFGHIJKLMNOPQ'
# while num > 0:
#     num27 = alph[num % 27] + num27
#     if (num % 27) % 2 == 0 and (num % 27) <= 25:
#         summ += num % 27
#     num //= 27
# print(summ)

max_x = ''
max_quantity = 0
for x in '0123456789ABCDEFGHIGKLMNOPQRSTUVWXY':
    num = int('6' + x + 'QR' + x, 35) + int(x + '59SH', 35) + int('PH' + x + '69YW', 35)
    digit_str = str(num)
    max_freq = 0
    digit_max = 0
    for i in range(10):
        freq = digit_str.count(str(i))
        if freq > max_freq or (freq == max_x and i > digit_max):
            max_freq = freq
            digit_max = i

    if digit_max != 0 and num % (digit_max ** 2) == 0:
        q = num // (digit_max ** 2)
        if x > max_x:
            max_x = x
            max_quantity = q

print(max_quantity)
