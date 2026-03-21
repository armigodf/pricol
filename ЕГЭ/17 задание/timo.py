with open('timo.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    for x, y in zip(nums, nums[1:]):
        if (x % 85 + y % 85) == min(nums):
            count += 1
            maxi = max(maxi, x + y)
    print(count, maxi)
