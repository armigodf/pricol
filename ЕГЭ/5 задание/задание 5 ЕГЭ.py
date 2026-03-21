# res = []
# for n in range(1, 50):
#     r = bin(n)[2:]
#     r = r + str(r.count('1') % 2)
#     r = r + str(r.count('1') % 2)
#     r = int(r, 2)
#     if r > 83:
#         res.append(r)
# print(min(res))

# ces = []
# res = []
# for n in range(1, 111):
#     r = bin(n)[2:]
#     r = r.replace('0', '00').replace('1', '11')
#     r = int(r, 2)
#     if r > 32:
#         ces.append(n)
#         res.append(r)
# print(min(res))
