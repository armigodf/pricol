# a = [1, 2, 4, 11, 6, 7, 9, 11, 32, 4, 4, 4, 9]
# uniq_a = []
# for i in range(len(a)):
#     b = a[i]
#     povt = False
#     for j in range(len(uniq_a)):
#         if uniq_a[j] == b:
#             povt = True
#             break
#     if not povt:
#         uniq_a.append(b)
#         count = 0
#         for k in range(len(a)):
#             if a[k] == b:
#                 count += 1
#         print(f"{b}:{count}")


# a = [1, 2, 4, 11, 6, 7, 9, 11, 32, 4, 4, 4, 9]
# slovar = {}
#
# for i in a:
#     if i in slovar:
#         slovar[i] += 1
#     else:
#         slovar[i] = 1
# print(slovar)


# def f(x:str):
#     a = 0
#     for elm in x.lower():
#         a += ord(elm) - ord('a')

# 1 задание
# print([x ** 2 for x in map(int, input("Введите числа через пробел: ").split())])
#
#
# # 2 задание
# def sqr(n):
#     for i in n:
#         b = int(i) ** 2
#         print(b, end=" ")
#
#
# a = input("Введите числа через пробел: ").split()
#
# sqr(a)


print([i**2 if i < 0 else i for i in map(int, input("введите циферки: ").split()) if 10 <= abs(i) <= 99])
