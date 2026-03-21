with open('17.5.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    chislo = 100000000000000
    for i in nums:
        if abs(i) % 10 == 5:
            chislo = min(chislo, i)
    for x, y in zip(nums, nums[1:]):
        if (abs(x) % 10 == abs(y) % 10) and (abs(x) % 10 == 9 or abs(y) % 10 == 9) and ((x**2 + y**2) < chislo ** 2):
            count += 1
            sqrt = max(sqrt, x**2 + y**2)
    print(sqrt, count)


# with open('17.7.txt') as f:
#     nums = [int(num) for num in f]
#     count = 0
#     chislo = 100000000000000
#     for i in nums:
#         if i % 10 == 6:
#             chislo = min(chislo, i)
#     for x, y in zip(nums, nums[1:]):
#         for x in '01234567':
#             for y in '01234567':
#                 if (int(x) % 10 == int(y) % 10) and ((int(x) % 9 == 0 and int(y) % 11 == 0) or (int(x) % 11 == 0 and \
#                 int(y) % 9 == 0) and int(x) % 99 != 0 and int(y) % 99 != 0) and (int(x) ** 2 + int(y) ** 2 <= chislo ** 3):
#                     count += 1
#                     sqrt = min(str(int(x) + int(y)))
#     print(count, sqrt)


# with open('17.3.3.txt') as f:
#     nums = [int(num) for num in f]
#     podh = []
#     for x, y, z in zip(nums, nums[1:], nums[2:]):
#         if len(str(x)) == 4 and len(str(y)) == 4 and len(str(z)) == 4:
#             sum1 = sum([int(num) for num in str(x)])
#             sum2 = sum([int(num) for num in str(y)])
#             sum3 = sum([int(num) for num in str(z)])
#             if sum1 != sum2 and sum2 != sum3 and sum1 != sum3:
#                 if str(x + y + z) == str(x + y + z)[::-1]:
#                     podh.append(sum1)
#                     podh.append(sum2)
#                     podh.append(sum3)
# print(len(podh) // 3, max(podh))


# with open('17.statgrad.txt') as f:
#     nums = [int(num) for num in f]
#     podh = []
#     count = 0
#     min_three = min(nums) % 3
#     max_seven = max(nums) % 7
#     for x, y in zip(nums, nums[1:]):
#         if ((x % 3 == min_three) + (y % 3 == min_three) >= 1) and ((y % 7 == max_seven) + (x % 7 == max_seven) >= 1):
#             count += 1
#             podh.append(x + y)
#     print(count)
#     print(max(podh))


# with open('17.9070.txt') as f:
#     nums = [int(num) for num in f]
#     h_f = [nums[x] for x in range(len(nums) // 2)]
#     h_s = [nums[-x - 1] for x in range(len(nums) // 2)]
#     scnd_ysl = 10000000000000
#     podh = []
#     count = 0
#     for x, y in zip(h_f, h_s):
#         if (99 < x < 1000) and (99 < y < 1000):
#
#             for i in str(x, y):
#                 if x.count(i) > 1 and y.count(i) > 1:

