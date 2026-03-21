from itertools import product
#
#
# cnt = 0
# for i in product('БЛАГОВЕЩНСК', repeat = 6):
#     a = ''.join(i)
#     if any(x in a for x in['ЩА', 'АЩ'])
#
# print(319038)


# cnt = 0
# for i in product('СВЕТЛАН', repeat=8):
#     word = ''.join(i)
#     if word.count('С') == 1 and word.count('В') == 1 and word.count('Е') == 1 and word.count('Т') == 1 and \
#             word.count('Л') == 1 and word.count('Н') == 1 and word.count('А') == 2 and word.count('АА') == 0:
#         cnt += 1
# print(cnt)


# cnt = 0
# for i in product('012345678', repeat=5):
#     word = ''.join(i)
#     if word[0] != '1' and word[0] != '3' and word[0] != '5' and word[0] != '7' and word[0] != '0':
#         if word[-1] != '1' and word[-1] != '8':
#             if word.count('3') <= 1:
#                 cnt += 1
# print(cnt)


# cnt = 0
# for i in product('01234567', repeat=5):
#     word = ''.join(i)
#     word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н')
#     if word[0] != '0' and word.count('6') == 1 and word.count('н6') == 0 and word.count('6н') == 0:
#         cnt += 1
# print(cnt)


# count = 0
# for i in product('0123456789AB', repeat=5):
#     word = ''.join(i)
#     if word[0] != '0' and word.count('7') == 1 and ((word.count('9') + word.count('A') + word.count('B')) <= 3):
#         count += 1
# print(count)


count = 0
for i in product('012345', repeat=6):
    word = ''.join(i)
    word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н')
    if word[0] != '0' and word.count('2н') == 0 and word.count('н2') == 0 and word.count('2') == 1:
        count += 1
print(count)
