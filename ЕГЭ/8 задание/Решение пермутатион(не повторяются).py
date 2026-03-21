from itertools import permutations

# count = 0
# for i in permutations('ЕГЭ204', 5):
#     count += 1
# print(count)


# count = 0
# for i in permutations('ABCDEF', 5):
#     word = ''.join(i)
#     if word[0] != 'A' and word[0] != 'E' and word[-1] != 'A' and word[-1] != 'E':
#         count += 1
#         print(count)


# count = 0
# for i in permutations('01234567', 5):
#     word = ''.join(i)
#     if word[0] != '0':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('0123456789ABCDEF', 4):
#     word = ''.join(i)
#     if word[0] != '0':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч').replace('A', 'ч').replace('C', 'ч').replace('E', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н').replace('9', 'н').replace('B', 'н').replace('D', 'н').replace('F', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('0234567', 5):
#     word = ''.join(i)
#     if word[0] != '0':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч')
#         word = word.replace('3', 'н').replace('5', 'н').replace('7', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)  # 864


# count = 0
# for i in permutations('0123456789A', 5):
#     word = ''.join(i)
#     if word[0] != '0':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч').replace('A', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н').replace('9', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('0123456789', 6):
#     word = ''.join(i)
#     if word[0] != '0' and int(word) % 5 == 0:
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н').replace('9', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('ЮЛИЙ', 5):
#     word = ''.join(i)
#     if (word[0] == 'Л' or word[0] == 'Й') and (word[-1] == 'Ю' or word[-1] == 'И'):
#         count += 1
# print(count)


# count = 0
# for i in permutations('0123456789', 4):
#     word = ''.join(i)
#     if word[0] != '0':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н') .replace('5', 'н') .replace('7', 'н') .replace('9', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('01234567', 5):
#     num = ''.join(i)
#     if num[0] != '0':
#         num = num.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч')
#         num = num.replace('1', 'н').replace('3', 'н') .replace('5', 'н') .replace('7', 'н')
#         if num.count('чч') == 0 and num.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('0123456789A', 6):
#     word = ''.join(i)
#     if word[0] != '0' and word[-1] == '7':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч').replace('A', 'ч')
#         if word.count('чч') >= 1:
#             count += 1
# print(count)


# count = 0
# for i in permutations('0123456789A', 5):
#     word = ''.join(i)
#     if word[0] != '0':
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч').replace('A', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н').replace('9', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


# count = 0
# for i in permutations('0123456789', 5):
#     word = ''.join(i)
#     if word[0] != '0' and word.count('5') == 0:
#         word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч')
#         word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н').replace('9', 'н')
#         if word.count('чч') == 0 and word.count('нн') == 0:
#             count += 1
# print(count)


count = 0
for i in permutations('012345678', 6):
    word = ''.join(i)
    if word[0] != '0':
        word = word.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч').replace('8', 'ч')
        word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н')
        if word.count('чч') == 0 and word.count('нн') == 0:
            count += 1
print(count)
