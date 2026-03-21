# for x in range(175457, 175506):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#         if len(deli) > 0:
#             break
#     if len(deli) == 0:
#         print(x)
#
#
# count = 0
# for x in range(93329, 93403):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 5:
#         count += 1
# print(count)


# count = 0
# for x in range(45869, 46054):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 4:
#         count += 1
# print(count)


# count = 0
# for x in range(65896, 65935):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 6:
#         print(deli)


# def num_m(x):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) > 0:
#         return max(deli) + min(deli)
#     else:
#         return 0
#
#
# count = 0
# for x in range(800000, 10**6):
#     if num_m(x) % 10 == 4:
#         print(x, num_m(x))
#         count += 1
#     if count == 5:
#         break


# count = 0
# for x in range(90556, 90645):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 10:
#         count += 1
# print(count)


# for x in range(312614, 312652):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 6:
#         print(deli)


# for x in range(65941, 66124):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 8:
#         print(x)


# for x in range(27144, 27151):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 2:
#         print(deli)


# count = 0
# for x in range(69646, 69803):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 5:
#         count += 1
# print(count)


# for x in range(25857, 25909):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 2:
#         print(x)


# count = 0
# for x in range(65106, 65149):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 6:
#         count += 1
# print(count)


# for x in range(65896, 65935):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 6:
#         print(deli)


# count = 0
# for x in range(69646, 69803):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 5:
#         count += 1
# print(count)


# for x in range(312614, 312652):
#     deli = []  #  ОШИБКА В ЗАДАНИЕ
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 6:
#         print(deli)


# for x in range(65914, 66123):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 8:
#         print(x, deli)

# for x in range(340000, 500000):
#     deli = []
#     for i in range(14, x, 10):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) != 0:
#         print(x, deli)


# for x in range(320000, 500000):
#     deli = []
#     for i in range(13, x, 10):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) != 0:
#         print(x, deli)


# for x in range(214361, 214381):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 6:
#         print(x, deli)


# for x in range(185311, 185331):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 4:
#         print(x, deli)


# n = 11000000
# cnt = 0
# while cnt < 5:
#     n += 1
#     m = -1
#     lst = []
#     for i in range(2, int(n**0.5)):
#         if n % i == 0:
#             lst.append(i)
#         if len(lst) == 2:
#             m = n / lst[0] + n / lst[1]
#             break
#     if len(lst) == 1:
#         m = lst[0] + n / lst[0]
#     if 0 < m < 8000:
#         print(int(m))
#         cnt += 1


# for x in range(24950, 25097):
#     deli = []
#     for i in range(2, x):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 8:
#         print(x, deli)


# for x in range(95632, 95651):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0 and i % 2 != 0:
#             deli.append(i)
#     if len(deli) == 6:
#         print(x, deli)


# for x in range(110203, 110246):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0 and i % 2 == 0:
#             deli.append(i)
#     if len(deli) == 4:
#         print(x, deli)

# def maxmin(n):
#     deli = []
#     for i in range(2, n):
#         if n % i == 0:
#             deli.append(i)
#     if len(deli) > 0:
#         return max(deli) + min(deli)
#     else:
#         return 0
#
#
# for x in range(700000, 1000000):
#     if maxmin(x) % 10 == 8:
#         print(x, maxmin(x))


# def summoner(n):
#     deli = []
#     for i in range(2, n):
#         if n % i == 0:
#             deli.append(i)
#     if len(deli) > 0:
#         return sum(deli)
#     else:
#         return 0
#
#
# for x in range(500000, 1000000):
#     if summoner(x) % 10 == 7:
#         print(x, summoner(x))


# def summa(n):
#     deli = []
#     for i in range(2, n):
#         if n % i == 0:
#             deli.append(i)
#     if len(deli) > 0:
#         return sum(deli)
#     else:
#         return 0
#
#
# for x in range(500100, 500450):
#     if summa(x) > 2 * x:
#         print(x)


# def minmax(n):
#     deli = []
#     for i in range(2, n):
#         if n % i == 0:
#             deli.append(i)
#     if len(deli) > 0:
#         return deli[0] + deli[-1]
#     else:
#         return 1
#
#
# for x in range(300000, 500000):
#     if minmax(x) % 17 == 0:
#         print(x, minmax(x))


# def minmax(n):
#     deli = []
#     for i in range(2, n):
#         if n % i == 0:
#             deli.append(i)
#     if len(deli) > 0:
#         return deli[0] + deli[-1]
#     else:
#         return 0
#
#
# for x in range(800000, 1000000):
#     if minmax(x) % 10 == 4:
#         print(x, minmax(x))


# for x in range(1111, 11112):
#     deli = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             deli.append(i)
#     if len(deli) == 5:
#         print(x, deli)


print(bin(252)[2:])