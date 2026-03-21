# with open('9070.txt') as f:
#     nums = [int(num) for num in f]
#     count = 0
#     maxi = 0
#     for x, y in zip(nums, nums[1:]):
#         if (x % 5 == 0 and y % 5 != 0) or (x % 5 != 0 and y % 5 == 0):
#             count += 1
#             maxi = max(maxi, x + y)
#     print(count, maxi)


# with open('9080.txt') as f:
#     nums = [int(num) for num in f]
#     count = 0
#     maxi = 0
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if (nums[i] * nums[j]) % 37 == 0:
#                 count += 1
#                 maxi = max(maxi, nums[i] + nums[j])
#     print(count, maxi)


with open('9090.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    max_spiska = 0
    for i in range(len(nums)):
        if 99 < nums[i] < 1000:
            max_spiska = max(max_spiska, nums[i])
    for x, y in zip(nums, nums[1:]):
        if ((99 < x < 1000) or (99 < y < 1000)) and (((x + y) % max_spiska) == 0):
            count += 1
            maxi = max(maxi, x + y)
    print(count, maxi)
