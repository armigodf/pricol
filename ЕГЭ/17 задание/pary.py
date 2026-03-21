with open('pary.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    for x, y in zip(nums, nums[1:]):
        if ((x % 35) + (y % 35)) == min(nums):
            count += 1
            maxi = max(maxi, x + y)
    print(count, maxi)
