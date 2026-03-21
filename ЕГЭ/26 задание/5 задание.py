f = open('Задание 26_5.txt')
n = int(f.readline())
nums = sorted([int(i) for i in x.split()] for x in f)
maxi = 0
for i in range(1, n):
    r, m = nums[i-1]
    if r == nums[i][0] and nums[i][1] - m == 14:
        if r > maxi:
            maxi, mini = r, m
print(maxi, mini+1)
f.close()
