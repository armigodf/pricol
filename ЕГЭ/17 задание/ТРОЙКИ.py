with open('17.2.txt') as f:
    count = 0
    nums = [int(num) for num in f]
    max_dd = max([num for num in nums if abs(num) % 100 == 29])
    for x, y, z in zip(nums, nums[1:], nums[2:]):
        if

