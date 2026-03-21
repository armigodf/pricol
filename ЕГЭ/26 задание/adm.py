f = open('adm.txt')
vmest, n = map(int, f.readline().split())
users = []
users_in = []
for s in f:
    users.append(int(s))
users.sort()
for i in range(len(users)):
    if (sum(users_in) + users[i]) <= vmest:
        users_in.append(users[i])
    elif (sum(users_in[:-1]) + users[i]) <= vmest:
        del users_in[-1]
        users_in.append(users[i])
print(len(users_in), max(users_in))
f.close()
