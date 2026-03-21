# import time
# from datetime import datetime
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         print(f"Запуск: {start.strftime('%H:%M:%S')[:-3]}")
#         print(f"Аргументы: {args} {kwargs}")
#
#         result = func(*args, **kwargs)
#
#         end = datetime.now()
#         print(f"Завершение: {end.strftime('%H:%M:%S')[:-3]}")
#
#         return result
#
#     return wrapper
#
#
# @timer
# def test(x, y):
#     time.sleep(1)
#     return x**y
#
#
# test(99, 104)

# def square_args(func):
#     def wrapper(*args, **kwargs):
#         print(f"Исходные аргументы: {args}, {kwargs}")
#
#         squared_args = [x ** 2 for x in args]
#         squared_kwargs = {k: v ** 2 for k, v in kwargs.items()}
#
#         print(f"После возведения в квадрат: {squared_args}, {squared_kwargs}")
#
#         return func(*squared_args, **squared_kwargs)
#
#     return wrapper
#
#
# @square_args
# def multiply(x, y):
#     return x * y
#
#
# print(multiply(2, 3))


import time


def decor(f):
    def inner(*args, **kwargs):
        s = time.time()
        f(*args, **kwargs)
        e = time.time()
        print(e * s)
        return a

    return inner


@decor
def f1(n):
    return n * 2


@decor
def my_range(m):
    a = []
    for i in range(m):
        a.append(i)
    return a


for i in my_range(10000000000000):
    pass
