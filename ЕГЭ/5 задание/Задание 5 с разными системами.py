# def traslator(num, ss=3):
#     num_in_ss = ''
#     while num > 0:
#         ost = num % ss
#         num_in_ss = str(ost) + num_in_ss
#         num = num // ss
#     return num_in_ss


# ces = []
# res = []
# for n in range(1, 111):
#     r = traslator(n)
#     if n % 3 == 0:
#         r = '1' + r + '02'
#     else:
#         r = r + traslator(((n % 3) * 4))
#     r = int(r, 3)
#     if r < 199:
#         ces.append(n)
#         res.append(r)
# print(max(ces))


# def tri(num, ss=3):
#     num_in_ss = ''
#     while num > 0:
#         ost = num % ss
#         num_in_ss = str(ost) + num_in_ss
#         num = num // ss
#     return num_in_ss


# ces = []
# res = []
# for n in range(1, 111):
#     r = tri(n)
#     if n % 3 == 0:
#         r = r + r[-3:]
#     else:
#         r = r + tri(((n % 3) * 3))
#     r = int(r, 3)
#     if r > 150:
#         ces.append(n)
#         res.append(r)    # ОТВЕТ: 9
# print(min(ces))


# ces = []
# res = []
# for n in range(1, 111):
#     r = bin(n)[2:]
#     if n % 3 == 0:
#         r = r + r[-3:]
#     else:
#         r = r + bin(((n % 3) * 3))[2:]
#     r = int(r, 2)
#     if r >= 76:
#         ces.append(n)
#         res.append(r)
# print(min(ces))


# ces = []
# res = []
# for n in range(1, 111):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if n <= 12:
#         ces.append(n)
#         res.append(r)
# print(max(res))


# ces = []
# res = []
# for n in range(1, 111):
#     n = (n - (n % 8)) + (n % 2)
#     r = bin(n)[2:]
#     r = r + str(r.count('1') % 2)
#     r = r + str(r.count('1') % 2)
#     r = int(r, 2)
#     if r > 90:
#         ces.append(n)
#         res.append(r)
# print(min(res))


# def chetiri(num):
#     num_per = ''
#     while num > 0:
#         s = num % 4
#         num_per = str(s) + num_per
#         num = num // 4
#     return num_per
#
#
# ces = []
# res = []
# for n in range(1, 111):
#     r = chetiri(n)
#     if n % 4 == 0:
#         r = r + r[-2:]
#     else:
#         r = r + chetiri((n % 4) * 2)
#     r = int(str(r), 4)
#     if r >= 1025:
#         res.append(r)
#         ces.append(n)
# print(min(ces))


# def chetiri(num):
#     num_per = ''
#     while num > 0:
#         s = num % 4
#         num_per = str(s) + num_per
#         num = num // 4
#     return num_per
#
#
# ces = []
# res = []
# for n in range(1, 111):
#     r = chetiri(n)
#     if n % 4 == 0:
#         r = r + r[-2:]
#     else:
#         r = r + chetiri((n % 4) * 2)
#     r = int(r, 4)
#     if r < 369:
#         res.append(r)
#         ces.append(n)
# print(max(ces))


# def piat(num):
#     num_per = ''
#     while num > 0:
#         s = num % 5
#         num_per = str(s) + num_per
#         num = num // 5
#     return num_per
#
#
# ces = []
# res = []
# for n in range(1, 111):
#     r = piat(n)
#     if n % 7 == 0:
#         r = r + r[-2:]
#     else:
#         r = r + piat((n % 7) * 7)
#     r = int(r, 5)
#     if r > 1234:
#         res.append(r)
#         ces.append(n)
# print(min(ces))


# def tri(num):
#     num_per = ''
#     while num > 0:
#         s = num % 3
#         num_per = str(s) + num_per
#         num //= 3
#     return num_per
#
#
# ces = []
# res = []
# for n in range(1, 111):
#     r = tri(n)
#     if n % 3 == 0:
#         r = r + r[-3:]
#     else:
#         r = r + tri((n % 3) * 3)
#     r = int(r, 3)
#     if r > 150:
#         res.append(r)
#         ces.append(n)
# print(min(ces))


# def tri(num):
#     nums = ''
#     while num > 0:
#         nums = str(num % 3) + nums
#         num //= 3
#     return nums
#
#
# ces = []
# res = []
# for n in range(1, 1111):
#     r = tri(n)
#     if n % 7 == 0:
#         r = r + r[-2:]
#     if n % 7 != 0:
#         r = r + tri((n % 7) * 3)
#     r = int(r, 3)
#     if r > 213:
#         res.append(r)
#         ces.append(n)
# print(min(ces))


# def tri(num):
#     num3 = ''
#     while num > 0:
#         num3 = str(num % 3) + num3
#         num //= 3
#     return num3


def f(num):
    num3 = ''
    while num > 0:
        num3 = str(num % 3) + num3
        num //= 3
    return num3
