# def f(a, b, m):
#     if a + b >= 118 or m > 2:
#         return m == 2  #РАССМАТРИВАЕМ ВАНЮ
#     return any([f(a+1,b,m+1), f(a+4,b,m+1), f(a*3,b,m+1), f(a,b+1,m+1), f(a,b+4,m+1), f(a,b*3,m+1)])
#
#
# for i in range(1, 118):
#     if f(10, i,  0):
#         print(i)


# def f(a, b, m):
#     if a + b >= 118 or m > 3:
#         return m == 3  #РАССМАТРИВАЕМ ПЕТЮ
#     if m % 2 == 1:
#         return all([f(a + 1, b, m + 1), f(a + 4, b, m + 1), f(a * 3, b, m + 1), f(a, b + 1, m + 1), f(a, b + 4, m + 1),
#                     f(a, b * 3, m + 1)])
#     return any([f(a+1,b,m+1), f(a+4,b,m+1), f(a*3,b,m+1), f(a,b+1,m+1), f(a,b+4,m+1), f(a,b*3,m+1)])
#
#
# for i in range(1, 118):
#     if f(10, i,  0):
#         print(i)


def f(a, b, m):
    if a + b >= 118 or m > 4:
        return m == 2 or m == 4  #РАССМАТРИВАЕМ ПЕТЮ
    if m % 2 == 0:
        return all([f(a + 1, b, m + 1), f(a + 4, b, m + 1), f(a * 3, b, m + 1), f(a, b + 1, m + 1), f(a, b + 4, m + 1),
                    f(a, b * 3, m + 1)])
    return any([f(a+1,b,m+1), f(a+4,b,m+1), f(a*3,b,m+1), f(a,b+1,m+1), f(a,b+4,m+1), f(a,b*3,m+1)])


for i in range(1, 118):
    if f(10, i,  0):
        print(i)
