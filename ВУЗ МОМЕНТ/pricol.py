# def func1(a, b):
#     a[0].append(b)
#     a.append(10)
#
#
# a = [[1], 2, 3]
# b = a.copy()
# func1(b, 4)
# print(a)
# print(b)


# a = [[[1]] * 3] * 3
# b = [[1 for _ in range(3)] for _ in range(3)]
# a[0][0] = 5
# print(a)
# print(b)


# a = [7 * 2 ** i for i in range(int(input("количесво чисел в масиве ")))]
# print(a)
#
# a = [i % 2 for i in range(int(input("количесво чисел в масиве ")))]
# print(a)
#
# a = [i ** 2 for i in range(int(input("количесво чисел в масиве ")))]
# print(a)


def gsd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gsd(588, 108))
