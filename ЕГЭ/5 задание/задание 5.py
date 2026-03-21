# res = []
# for n in range(1, 100):
#     r = bin(n)[2:]  # Строится двоичная запись числа N.
#     if n % 2 == 0:  # Если N — чётное, то в конец полученной записи (справа) дописывается 0, в начало 1;
#         r = '1' + r + '0'
#     else:  # если N нечётное, в конец и начало дописывается по две единицы.
#         r = '11' + r + '11'
#     r = int(r, 2)
#     if r > 52:
#         res.append(r)
# print(min(res))


# ces = []
# res = []
# for n in range(0, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r += '00'
#     else:
#         r += '11'
#     r = int(r, 2)
#     if r > 134:
#         ces.append(n)
#         res.append(r)
# print((ces))


# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     r = r + str(r.count('1') % 2)
#     r = r + str(r.count('1') % 2)
#     r = int(r, 2)
#     if r > 97:
#         res.append(r)
# print(res)


# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r + '01'
#     else:
#         r = r + '10'
#     r = int(r, 2)
#     if r > 81:
#         res.append(r)
# print(res)


# res = []
# ces = []
# for n in range(1, 1000):
#     r = bin(4 * n)[2:]
#     r = r + str(r.count('1') % 2)
#     r = r + str(r.count('1') % 2)
#     r = int(r, 2)
#     if r > 129:
#         ces.append(n)
#         res.append(r)
# print(ces)


# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     r = r + str(r.count('1') % 2)
#     r = r + str(r.count('1') % 2)
#     r = int(r, 2)
#     if r > 396:
#         res.append(r)
# print(res)


# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 3 == 0:
#         r = r + r[-3:]
#     else:
#         r = r + bin((n % 3)*3)[2:]
#     r = int(r, 2)
#     if r > 151:
#         res.append(r)
# print(min(res))


# ces = []
# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 35:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 217:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 86:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 424:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(1, 1111):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '1' + r + '0'
#     if n % 2 != 0:
#         r = '11' + r + '11'
#     r = int(r, 2)
#     if r > 451:
#         ces.append(n)
#         res.append(r)
# print(min(res))


# ces = []
# res = []
# for n in range(1, 1111):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '1' + r + '0'
#     if n % 2 != 0:
#         r = '11' + r + '11'
#     r = int(r, 2)
#     if r > 102:
#         ces.append(n)
#         res.append(r)
# print(min(res))


# ces = []
# res = []
# for n in range(1, 1111):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r + '00'
#     if n % 2 != 0:
#         r = r + '11'
#     r = int(r, 2)
#     if r <= 71:
#         ces.append(n)
#         res.append(r)
# print(max(ces))


# ces = []
# res = []
# for n in range(2, 1111):
#     r = bin(n)[2:]
#     r = r + r[-2]
#     r = r + r[1]
#     r = int(r, 2)
#     if r > 75:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(2, 1111):
#     r = bin(n)[2:]
#     r = r + r[-2]
#     r = r + r[1]
#     r = int(r, 2)
#     if r > 108:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(2, 1111):
#     r = bin(n)[2:]
#     r = r + r[-2]
#     r = r + r[1]
#     r = int(r, 2)
#     if r > 150:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(2, 1111):
#     r = bin(n)[2:]
#     r = r + r[-2]
#     r = r + r[1]
#     r = int(r, 2)
#     if r > 180:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


ces = []
res = []
for n in range(2, 1111):
    r = bin(n)[2:]
    if n % 7 == 0:
        r = r + '01'
    else:
        r = r + f'{bin(n // 7)[2:]}'
    r = int(r, 2)
    if r <= 1300 and n % 2 != 0:
        ces.append(n)
        res.append(r)
print(max(ces))
