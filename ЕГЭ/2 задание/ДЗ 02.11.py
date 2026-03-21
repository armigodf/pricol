# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if (((x and not (y)) or (w <= z)) == (z == x)) == 1:
#                     print(z, y, w, x)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if (((w <= (not(x))) == (z <= y)) and (y or w)) == 1:
#                     print(x, w, y, z)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((x or not(y)) and not (w == z) and w) == 1:
#                     print(x, y, z, w)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((not(x) or not(y)) and not(x == z) and w) == 1:
#                     print(w, x, y, z)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((x and not(y)) or (y == z) or w) == 0:
#                     print(y, x, w, z)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((x or y) and not(y == z) and not(w)) == 1:
#                     print(x, z, y, w)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if (((not(x)) or y or z) == ((not(y)) and z and w)) == 1:
#                     print(y, w, z, x)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((x or not(z)) and (x == (not(w))) and (x <= y)) == 1:
#                     print(z, y, w, x)


# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if (((x <= y) == (w <= x)) and (z <= w)) == 1:
#                     print(y, z, w, x)


for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x <= y) == (y <= z)) and (y or w)) == 1:
                    print(x, z, w, y)
# x z w y