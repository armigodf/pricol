with open('17H.Y1.txt') as f:
    nums = [int(num) for num in f]
    maxi = max([i for i in nums if 9999 < i < 100000 and i % 100 == 17])
    count = 0
    mini = 11111111
    for x, y, z in zip(nums, nums[1:], nums[2:]):
        if abs(x) % 100 == 17 or abs(y) % 100 == 17 or abs(z) % 100 == 17:
            if (abs(x) + abs(y) + abs(z)) < maxi:
                count += 1
                mini = min(mini, x + y + z)
    print(count, mini)
