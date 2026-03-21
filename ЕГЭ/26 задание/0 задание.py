# f = open('26.txt')
# by = int(f.readline())
# box = sorted([int(s) for s in f], reverse=True)
# box_in = [box[0]]
# while len(box) > 0:
#     for i in range(1, by):
#         if box_in[-1] >= box[i] + 5:
#             box_in.append(box[i])
# print(len(box_in), min(box_in))

#
# f = open('26.txt')
# n = f.readline()
# cubes = sorted([int(i) for i in f], reverse=True)
# cubes_in = []
# while len(cubes) > 0:
#     block = [cubes.pop(0)]
#     for i in range(len(cubes)):
#         if block[-1] >= cubes[i] + 5:
#             block.append(cubes[i])
#             cubes[i] = ''
#     cubes = [x for x in cubes if x != '']
#     cubes_in.append(block)
# print(len(cubes_in), max(len(c) for c in cubes_in))



