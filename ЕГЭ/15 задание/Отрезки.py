# p = list(range(6, 30))
# q = list(range(15, 25))
# A = list(range(1000))
# for x in range(1000):
#     if (((x in p) == (x in q)) <= (not(x in A))) == 0:
#         A.remove(x)
# print(A)


# p = list(range(7, 15))
# q = list(range(9, 12))
# A = list(range(1000))
# for x in range(1000):
#     if (((x in p) == (x in q)) <= (not(x in A))) == 0:
#         A.remove(x)
# print(A)


# p = list(range(5, 19))
# q = list(range(10, 26))
# A = []
# for x in range(1000):
#     if (((x in p) and (x in q)) <= (x in A)) == 0:
#         A.append(x)
# print(A)


# p = list(range(130, 172))
# q = list(range(150, 186))
# A = []
# for x in range(1000):
#     if ((x in p) <= (((x in q) and (not(x in A))) <= (not(x in p)))) == 0:
#         A.append(x)
# print(A)


# p = list(range(9, 29))
# q = list(range(14, 20))
# A = list(range(1000))
# for x in range(1000):
#     if (((x in A) <= (x in p)) or (x in q)) == 0:
#         A.remove(x)
# print(A)


# p = list(range(27, 51))
# q = list(range(34, 50))
# A = list(range(1000))
# for x in range(1000):
#     if (((not(x in A)) <= (x in p)) <= ((x in A) <= (x in q))) == 0:
#         A.remove(x)
# print(A)


# p = list(range(18, 45))
# q = list(range(21, 59))
# A = []
# for x in range(1000):
#     if ((not(x in A)) <= (((x in p) and (x in q)) <= (x in A))) == 0:
#         A.append(x)
# print(A)


# p = list(range(19, 39))
# q = list(range(19, 59))
# A = []
# for x in range(1000):
#     if ((not (x in A)) <= (((x in p) and (x in q)) <= (x in A))) == 0:
#         A.append(x)
# print(A)


# p = list(range(21, 72))
# q = list(range(41, 102))
# A = []
# for x in range(1111):
#     if (not(not(x in A) and (x in p)) or (x in q)) == 0:
#         A.append(x)
# print(len(A))


# p = list(range(11, 62))
# q = list(range(51, 92))
# A = []
# for x in range(1111):
#     if (not(not(x in A) and (x in p)) or (x in q)) == 0:
#         A.append(x)
# print(len(A))


# p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# A = list(range(1000))
# for x in range(1111):
#     if (((x in A) <= (x in p)) or ((not(x in q)) <= (not(x in A)))) == 0:
#         A.remove(x)
# print(len(A))


# p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# q = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# A = list(range(1111))
# for x in range(1111):
#     if (((x in A) <= (x in p)) and ((x in q) <= (not(x in A)))) == 0:
#         A.remove(x)
# print(len(A))


e = list(range(18, 43))  # НАИМЕНЬШЕЕ
v = list(range(11, 18))
A = []
for x in range(1111):
    if ((x in e) <= ((not(x in v)) and (x in A))) == 0:
        A.append(x)
print(len(A))


p = list(range(10, 32))  # НАИБОЛЬШЕЕ
q = list(range(13, 21))
A = list(range(1111))
for x in range(1111):
    if (((x in A) <= (x in p)) or (x in q)) == 0:
        A.remove(x)
print(len(A))


# p = list(range(20, 51))
# q = list(range(30, 66))
# A = []
# for x in range(1111):
#     if ((not(x in A)) <= ((x in p) <= (not(x in q)))) == 0:
#         A.append(x)
# print(A)


# p = list(range(11, 42))
# q = list(range(24, 60))
# A = []
# for x in range(1111):
#     if (((x in p) and (x in q)) <= ((x in q) and (x in A))) == 0:
#         A.append(x)
# print(len(A))


# p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# A = list(range(1111))
# for x in range(1111):
#     if (((x in A) <= (x in p)) and ((not(x in q)) <= (not(x in A)))) == 0:
#         A.remove(x)
# print(A)
