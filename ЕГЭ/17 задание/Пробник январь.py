with open('Задание 17 (1).txt') as f:
    nums = [int(num) for num in f]
    maxi = 0
    count = 0
    for x, y in zip(nums, nums[1:]):
        if x % 7 == 0 or y % 7 == 0:
            count += 1
            maxi = max(maxi, x + y)
    print(count, maxi)
