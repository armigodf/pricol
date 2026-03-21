with open('пробник май.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    for x, y, z in zip(nums, nums[1:], nums[2:]):
        if min(x, y, z) % 3 == 0 and (x % 3 != 0 or x == min(x, y, z)) and (y % 3 != 0 or y == min(x, y, z)) and \
                (z % 3 != 0 or z == min(x, y, z)):
            if (x + y + z) % 7 == 2:
                count += 1
                maxi = max(maxi, x + y + z)
    print(count, maxi)
