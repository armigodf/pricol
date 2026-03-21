# with open(r"C:\Users\davyd\Downloads\9H.Y1.csv") as f:
#     count = 0
#     for line in f:
#         a = list(map(int, line.split(';')))
#         a.sort()
#         pov = [i for i in a if a.count(i) == 3]
#         nepov = [i for i in a if a.count(i) == 1]
#         chet = [x for x in a if x % 2 == 0]
#         nechet = [x for x in a if x % 2 != 0]
#         maximaliti = a[-1] + a[-2]
#         if ((len(pov) == 3 and len(nepov) == 3) + (len(chet) > len(nechet)) + (maximaliti > (sum(a) - maximaliti) * 2)) >= 2:
#             count += 1
#     print(count)


print(bin(208)[2:])

print(int('11111100', 2))