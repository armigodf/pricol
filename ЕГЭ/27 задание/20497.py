with open('20497B.txt') as f:
    f.readline()
    claster_1 = []
    claster_2 = []
    claster_3 = []
    claster_4 = []
    claster_5 = []

    for i in f:
        x, y = map(float, i.split())
        if -55 <= x <= -35 and -30 <= y <= 30:
            claster_1.append((x, y))
        if -40 <= x <= -22 and 42 <= y <= 110:
            claster_2.append((x, y))
        if -28 <= x <= -8 and -30 <= y <= 30:
            claster_3.append((x, y))
        if -10 <= x <= 10 and 45 <= y <= 110:
            claster_4.append((x, y))
        if 0 <= x <= 20 and -30 <= y <= 30:
            claster_5.append((x, y))


def cent_kr(cluster):
    x_kr, y_kr = 0, 0
    maxi = -1
    for i in range(len(cluster)):
        sum_way = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            sum_way += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if sum_way > maxi:
            maxi = sum_way
            x_kr, y_kr = x1, y1
    return x_kr, y_kr


x1, y1 = cent_kr(claster_1)
x2, y2 = cent_kr(claster_2)
x3, y3 = cent_kr(claster_3)
x4, y4 = cent_kr(claster_4)
x5, y5 = cent_kr(claster_5)


print(((x1 + x2 + x3 + x4 + x5) / 5) * 10000)
print(((y1 + y2 + y3 + y4 + y5) / 5) * 10000)
