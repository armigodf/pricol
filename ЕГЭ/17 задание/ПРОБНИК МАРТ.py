with open('ПРОБНИК МАРТ.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    mini = 100000
    for m in range(len(nums)):
        if nums[m] % 67 == 0 and nums[m] % 10 != 0 and nums[m] < mini:
            mini = nums[m]
    for x, y in zip(nums, nums[1:]):
        if (x % mini == 0) or (y % mini == 0):
            count += 1
            maxi = max(maxi, x + y)
    print(count, maxi)
