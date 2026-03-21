# f = open('les2.txt')
# n = int(f.readline())
# nums = sorted([int(i) for i in x.split()] for x in f)
# maxi = 0
# for i in range(1, n):
#     ryad, mesto = nums[i - 1]
#     if ryad == nums[i][0] and nums[i][1] - mesto == 2:
#         if ryad > maxi:
#             maxi, mini = ryad, mesto
# print(maxi, mini + 1)


f = open('les2.txt')
n, k = map(int, f.readline().split())
nums = sorted(list(map(int, f.readline().split())) for x in range(n))
maxi, mini = -1, 0
for x, y in zip(nums, nums[1:]):
    if x[0] == y[0] and y[1] - x[1] == k + 1:
        if x[0] > maxi:
            maxi = x[0]
            mini = x[1] + 1
print(maxi, mini)



#     ryad, mesto = nums[i - 1]
#     if ryad == nums[i][0] and nums[i][1] - mesto == k + 1:
#         if ryad > maxi:
#             maxi, mini = ryad, mesto
# print(maxi, mini + 1)


# for x, y in zip(nums, nums[1:]):