# s = list('ФАВОРИТ')
# s.sort()
# count = 0
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         word = a + b + c + d + e + f
#                         i += 1
#                         if a != 'О' and word.count('Р') == 2 and i % 2 == 0:
#                             count += 1
# print(count)


# s = list('АТОМ')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 word = a + b + c + d
#                 i += 1
#                 if word[0] == 'О':
#                     print(i)


# s = list('АБЗИ')
# s.sort()
# i = 1
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 word = a + b + c + d
#                 i += 1
#                 if a == 'И' and b == 'З' and c == 'Б' and d == 'А':
#                     print(i)


# s = list('МАРТ')
# s.sort()
# i = 1
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 word = a + b + c + d
#                 i += 1
#                 if a == 'М':
#                     print(i)


# s = list('КОМПЬЮТЕР')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     word = a + b + c + d + e
#                     i += 1
#                     if word.count('Ю') == 3 and word[-1] != 'Ь':
#                         print(i)


# s = list('КЛНТЭ')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         word = a + b + c + d + e + f
#                         i += 1
#                         if a == 'К' and b == 'К' and c == 'Л' and d == 'К' and e == 'К' and f == 'Н':
#                             print(i)


# s = list('РЕПЛИКА')
# s.sort()
# count = 0
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         word = a + b + c + d + e + f
#                         i += 1
#                         if i % 2 == 0 and a != 'К' and word.count('И') >= 2:
#                             count += 1
# print(count) #10892


# s = list('ФЛАМИНГО')
# s.sort()
# i = 0
# count = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     word = a + b + c + d + e
#                     i += 1
#                     if i % 2 != 0 and a != 'Н' and  word.count('О') <= 1:
#                         count += 1
# print(count)  #11907


# s = list('ИНТЕГРАЛ')
# s.sort()
# i = 0
# count = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     word = a + b + c + d + e
#                     i += 1
#                     if i % 2 != 0 and a != 'Т' and (word.count('Н') == 1 or word.count('Н') == 2):
#                         count += 1
# print(count)  #5992


# s = list('СОРНЯК')
# s.sort()
# i = 0
# count = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         word = a + b + c + d + e + f
#                         i += 1
#                         if word.count('К') <= 3 and word.count('Я') == 2:
#                             print(i)  # 73


# s = list('ПРАВО')
# s.sort()
# i = 1
# count = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 word = a + b + c + d
#                 count += 1
#                 if a == 'П':
#                     print(count) # 376


# s = list('БОРМША')
# s.sort()
# i = 0
# count = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         for t in s:
#                             word = a + b + c + d + e + f + t
#                             if word[1]
#                                 count += 1
#                                     print(word)


# s = list('SHOW')
# s.sort()
# i = 0
# count = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     word = a + b + c + d + e
#                     count += 1
#                     print(count)


# s = list('БЛАГОВЕЩНСК')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         word = a + b + c + d + e + f
#                         if word.count('ЩА') != 0 and word.count('АЩ') != 0 and word.count('ЩО') != 0 and \
#                                 word.count('ОЩ') != 0 and word.count('ЩЕ') != 0 and word.count('ЕЩ') != 0 and \
#                                 word.count('ЩГ') == 0 and word.count('ГЩ') == 0:
#                             i += 1
# print(i)


# s = list('01234')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         for g in s:
#                             word = a + b + c + d + e + f + g
#                             for k in range(len(word) - 1):
#                                 if (word[k] == word[k + 1]) and (a != '0'):
#                                     i += 1
#                                     break
# print(i)


# s = list('ПЧЕЛА')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 word = a + b + c + d
#                 if word[0] != 'А' and (word.count('А') >= 1 or word.count('Е') >= 1):
#                     i += 1
# print(i)


# s = list('ЭШОЯР')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         for g in s:
#                             word = a + b + c + d + e + f + g
#                             i += 1
#                             if i == 31:
#                                 print(word)


# s = list('ШАРИК')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     word = a + b + c + d + e
#                     if word[0] == 'А' and word[-1] == 'И' and word.count('К') == 1:
#                         i += 1
# print(i)


# s = list('ЦИТРУС')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     word = a + b + c + d + e
#                     i += 1
#                     if word.count('И') == 1 and word.count('ИУ') == 0 and word.count('УИ') == 0:
#                         print(i)


s = list('ЛАЙМ')
s.sort()
i = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    i += 1
                    if word.count('М') <= 1 and word.count('МЛ') == 0 and word.count('ЛМ') == 0:
                        print(i)


# s = list('012345678')
# s.sort()
# i = 0
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         word = a + b + c + d + e + f
#                         if word[0] != '0':
#                             i += 1
#                             w_copy = word
#                             word = word.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н')
#                             if (word.count('нн') == 0) and (i % 10 == 5):
#                                 print(w_copy)
