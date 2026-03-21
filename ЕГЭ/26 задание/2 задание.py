f = open('Задание 26_2.txt')
n = int(f.readline())
box = sorted([int(s) for s in f], reverse=True)
box_in = [box[0]]
for i in range(1, n):
    if box_in[-1] >= box[i] + 3:
        box_in.append(box[i])
print(len(box_in), min(box_in))
f.close()
