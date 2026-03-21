f = open('bag.txt')
iach = int(f.readline())
tyr = int(f.readline())
vrema = sorted([list(map(int, i.split())) for i in f])
# print(vrema)
count = 0
maxi = 0
posl = 0

for i in range(1, iach+1):
    con = 0
    for j in vrema:
        if j[0]-con >= 1 and j[0] > 0 and j[1] > 0:
            count += 1
            con = j[1]
            if j[0] > maxi:
                maxi = j[0]
                posl = i
            j[0] = 0
            j[1] = 0
print(count, posl)
f.close()
