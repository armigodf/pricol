# f = open('Задание 26_3.txt')
# n = f.readlines()
# points = []
# count = 0
# maxi = 0
# for s in f:
#     ryad, mesto = map(int, s.split())
#     points.append([ryad, mesto])
# points.sort()
# for i in range(1, len(points)):
#     if (points[i][0] == points[i - 1][0]) and (points[i][1] == points[i - 1][1]):
#         continue
#     elif (points[i][0] == points[i - 1][0]) and (points[i][1] - points[i - 1][1] == 2):
#         count += 1
#         if count > maxi:
#             ryad_m = points[i][0]
#             maxi = max(maxi, count)
#     else:
#         count = 1
#         print(maxi, ryad_m)
# f.close()

f = open('Задание 26_4.txt')
n = int(f.readline())
points = []  # sorted([int(i) for i in x.split()] for x in f)
count = 1
maxi = 1
for s in f:
    ryad, mesto = map(int, s.split())
    points.append([ryad, mesto])
points.sort()
for i in range(1, len(points)):
    if (points[i][0] == points[i - 1][0]) and (points[i][1] == points[i - 1][1]):
        continue
    elif (points[i][0] == points[i - 1][0]) and (points[i][1] - points[i - 1][1] == 2):
        count += 1
        if maxi < count:
            ryad_m = points[i][0]
            maxi = max(maxi, count)
    else:
        count = 1
print(maxi, ryad_m)
f.close()
