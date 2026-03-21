# with open('numbers.txt.txt') as f:
#     count = 0
#     scnd_ysl = 0
#     chislo = -1000000
#     nums = [int(num) for num in f]
#     for i in nums:
#         if abs(i) % 100 == 12:
#             chislo = max(chislo, i)
#     for h in range(len(nums) - 1):
#         if (((abs(nums[h]) % 100 == 12) and (abs(nums[h + 1]) % 100 != 12)) or ((abs(nums[h]) % 100 != 12) and \
#         (abs(nums[h + 1]) % 100 == 12))) and (nums[h] + nums[h + 1]) ** 2 < chislo ** 4:
#             count += 1
#             scnd_ysl = max(scnd_ysl, nums[h] + nums[h + 1])
#     print(count, scnd_ysl)

#
# with open('numbers.txt.txt') as f:
#     count = 0
#     scnd_ysl = 0
#     chislo = -1000000
#     nums = [int(num) for num in f]
#     for i in nums:
#         if abs(i) % 100 == 12:
#             chislo = max(chislo, i)
#     for h in range(len(nums) - 1):
#         if (((abs(nums[h]) % 100 == 12) and (abs(nums[h + 1]) % 100 != 12)) or ((abs(nums[h]) % 100 != 12) and \
#         (abs(nums[h + 1]) % 100 == 12))) and (nums[h] + nums[h + 1]) ** 2 < chislo ** 2:
#             count += 1
#             scnd_ysl = max(scnd_ysl, nums[h] + nums[h + 1])
#     print(count, scnd_ysl)


# with open('numbers.txt.txt') as f:
#     count = 0
#     scnd_ysl = 0
#     chislo = 100000000000
#     nums = [int(num) for num in f]
#     for i in nums:
#         if abs(i) % 1000 == 123:
#             chislo = min(chislo, i)
#     for h in range(len(nums) - 1):
#         if (((abs(nums[h]) % 1000 == 123) or (abs(nums[h]) % 1000 != 123)) or ((abs(nums[h]) % 1000 != 123) or \
#         (abs(nums[h]) % 1000 == 123))) and (abs(nums[h] ** 2 - nums[h - 1] ** 2)) < chislo ** 4:
#             count += 1
#             scnd_ysl = min(scnd_ysl, nums[h] + nums[h + 1])
#     print(count, scnd_ysl)


with open('numbers.txt.txt') as f:
    count = 0
    scnd_ysl = 10000000000000
    chislo = 100000000000
    nums = [int(num) for num in f]
    for i in nums:
        if abs(i) % 1000 == 123:
            chislo = min(chislo, i)
    for h in range(len(nums) - 1):
        if ((abs(nums[h]) % 1000 == 123) or (abs(nums[h + 1]) % 1000 == 123)) and (abs(nums[h] ** 2 - nums[h + 1] ** 2)) < chislo ** 4:
            count += 1
            scnd_ysl = min(scnd_ysl, nums[h] + nums[h + 1])
    print(count, scnd_ysl)
