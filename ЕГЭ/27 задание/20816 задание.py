with open('20816B.txt') as f:
    f.readline()
    claster_1 = []
    claster_2 = []
    claster_3 = []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        # if 0 <= x <= 6 and 4 <= y <= 10:
        #     claster_1.append((x, y))
        # if -7 <= x <= 0 and -9 <= y <= -2:
        #     claster_2.append((x, y))
        if -2 <= x <= 9 and -3 <= y <= 8:
            claster_1.append((x, y))
        if -15 <= x <= -5 and -10 <= y <= 0:
            claster_2.append((x, y))
        if -4 <= x <= 7 and -15 <= y <= -5:
            claster_3.append((x, y))


def centr_cl(cluster):
    x_cnt, y_cnt = 0, 0
    mini = 10**100
    for i in range(len(cluster)):
        sum_way = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            sum_way += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if sum_way < mini:
            mini = sum_way
            x_cnt, y_cnt = x1, y1
    return x_cnt, y_cnt


x1, y1 = centr_cl(claster_1)
x2, y2 = centr_cl(claster_2)
x3, y3 = centr_cl(claster_3)


print(((x1 + x2 + x3) / 3) * 10000)
print(((y1 + y2 + y3) / 3) * 10000)
