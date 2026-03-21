with open('пробник апрель.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    for x, y in zip(nums, nums[1:]):
        if x % 8 == 0 or y % 8 == 0:
            if (x + y) % 2 != 0:
                count += 1
                maxi = max(maxi, x + y)
    print(count, maxi)
