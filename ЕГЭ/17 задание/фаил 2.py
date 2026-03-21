with open('фаил 2.txt') as f:
    nums = [int(num) for num in f]
    max13 = max([i for i in nums if i % 100 == 13])
    count = 0
    maxi = 0
    for x, y, z in zip(nums, nums[1:], nums[2:]):
        if (len(str(x)) == 3 and len(str(y)) == 3 and len(str(z)) != 3) or (len(str(x)) == 3 and len(str(y)) != 3 and len(str(z)) == 3) or \
                (len(str(x)) != 3 and len(str(y)) == 3 and len(str(z)) == 3):
            if (x + y + z) <= max13:
                count += 1
                maxi = max(maxi, x + y + z)
    print(count, maxi)


