# f = open('Задание 26_14.txt')
# n, mon = f.readline().split()
# mon = int(mon)
# a_pr = []
# a_cnt = []
# for i in f:
#     if 'A' in i:




f = open('Задание 26_14.txt')
x, y = f.readline().split()
y = int(y)
for_B_price = []
for_B_kol = []
for i in f:
    if 'A' in i:
        a, b, c = i.split()
        print(a, b, c)
        y -= int(a) * int(b)
    else:
        a2, b2, c2 = i.split()
        for_B_price.append(int(a2))
        for_B_kol.append(int(b2))
mini = min(for_B_price)
index_mini = 0
for i in range(len(for_B_price)):
    if mini == for_B_price[i]:
        index_mini = i
kol_B = 0
while y > for_B_price[index_mini]:
    y -= for_B_price[index_mini]
    for_B_kol[index_mini] -= 1
    kol_B += 1
    if for_B_kol[index_mini] == 0:
        for_B_price[index_mini] = 1000000000
        mini = min(for_B_price)
        for i in range(len(for_B_price)):
            if mini == for_B_price[i]:
                index_mini = i
print(kol_B, y)
