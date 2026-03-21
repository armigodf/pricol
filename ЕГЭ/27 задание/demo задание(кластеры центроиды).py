with open('demo_2025_27_Б.txt') as f:
    f.readline()
    claster_1 = []
    claster_2 = []
    claster_3 = []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if 0 <= x <= 2.5 and 0 <= y <= 3:
            claster_1.append((x, y))
        if 5 <= x <= 8.5 and 4 <= y <= 7:
            claster_2.append((x, y))
        if 2 <= x <= 4.5 and 7 <= y <= 11:
            claster_3.append((x, y))


def cent_cl(cluster):
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


x1, y1 = cent_cl(claster_1)
x2, y2 = cent_cl(claster_2)
x3, y3 = cent_cl(claster_3)


print(((x1 + x2 + x3) / 3) * 10000)
print(((y1 + y2 + y3) / 3) * 10000)


# 10738.21226546789
# 30730.076059078103