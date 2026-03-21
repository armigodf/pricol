# with open('') as f:
#     n, m = int(f.readline().split())
#     boxes = []
#     for i in range(m):
#         red, blue = map(int, f.readline().split())
#         boxes.append([red, 'red'])
#         boxes.append([blue, 'blue'])
#     for i in range(n - m):
#         red = int(f.readline())
#         boxes.append([red, 'red'])
#     boxes.sort(reverse=True)
#     matr = [boxes[0]]
#     for box in boxes:
#         if matr[-1][0] - box[0] >= 3 and matr[-1][1] != box[1]:
#             matr.append(box)
#     print(len(matr), print(matr[-1]))


print(bin(240)[2:])
