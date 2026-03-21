with open('27_B_21720.txt') as f:
    f.readline()

    claster_1 = []
    claster_2 = []
    claster_3 = []

    for i in f:
        x, y = map(float, i.split())
        if -14 < x < -6 and 8 < y < 17:
            claster_1.append((x, y))
        if -6 < x < 3 and 2 < y < 10:
            claster_2.append((x, y))
        if -8 < x < 2 and -16 < y < -5:
            claster_3.append((x, y))


def cl_centr(claster):
    x_cnt, y_cnt = 0, 0
    mini = 10**100
    for i in range(len(claster)):
        sum_way = 0
        for j in range(len(claster)):
            x1, y1 = claster[i]
            x2, y2 = claster[j]
            sum_way += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if sum_way < mini:
            mini = sum_way
            x_cnt, y_cnt = x1, y1
    return x_cnt, y_cnt


x1, y1 = cl_centr(claster_1)
x2, y2 = cl_centr(claster_2)
x3, y3 = cl_centr(claster_2)

print(((x1 + x2 + x3) / 3) * 10000)
print(((y1 + y2 + y3) / 3) * 10000)
