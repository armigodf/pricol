f = open('Задание 26_12.txt')
gruz, n = map(int, f.readline().split())
cont = []
cont_in = []
for s in f:
    cont.append(int(s))
cont.sort()
for i in range(len(cont)):
    if (sum(cont_in) + cont[i]) <= gruz:
        cont_in.append(cont[i])
    elif (sum(cont_in[:-1]) + cont[i]) <= gruz:
        del cont_in[-1]
        cont_in.append(cont[i])
print(len(cont_in), max(cont_in))






# f = open('Задание 26_алгоритм решения.txt')
# vmest, n = map(int, f.readline().split())
# users = []
# users_in = []
# for s in f:
#     users.append(int(s))
# users.sort()
# for i in range(len(users)):
#     if (sum(users_in) + users[i]) <= vmest:
#         users_in.append(users[i])
#     elif (sum(users_in[:-1]) + users[i]) <= vmest:
#         del users_in[-1]
#         users_in.append(users[i])
# print(len(users_in), max(users_in))
# f.close()


# f = open('26.txt')
# l = f.readline()
# limit = int(l.split()[0])
# n = int(l.split()[1])
# a = [int(x) for x in f.readlines()]
# a.sort()
# ns = 0
# k = 0
# for i in a:
#     if ns + i <= limit:
#         ns += i
#         k += 1
#         temp = i
#     else:
#         ns -= temp
#         for j in a:
#             if ns + j <= limit:
#                 temp = j
#             else:
#                 break
#         break
# print(k, temp)
