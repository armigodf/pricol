# a = [4, 1, 8, 7, 8, 9, 8, 9]
# sum1 = 0
# prod1 = 1
# # for i in range(int(input("Введите число чисел в масиве: "))):
# #     a.append(i)
# # print(a)
#
#
# for j in range(len(a)):
#     if j % 2 == 0:
#         sum1 += j
# print(sum1)
#
# for i in range(1, len(a), 2):
#     prod1 *= a[i]
# print(prod1)  # умн нечётных индексов
#
# print(a.count(max(a)))   # считаем количесво максимальных

# def kv(n):
#     i = 0
#     while i**2 < n:
#         yield i
#         i += 1

# def nech(n):
#     i = 0
#     for i in range(1, n + 1):
#         yield 2 * i - 1


def fib(n):
    i = 0
    a = 0
    b = 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


n = int(input("чиселко: "))
print(list(fib(n)))
