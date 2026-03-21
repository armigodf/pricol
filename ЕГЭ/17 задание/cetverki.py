with open('chetverki.txt') as f:
    nums = [int(num) for num in f]
    de = len([i for i in nums if i % 2074 == 0])
    count = 0
    maxi = 0
    for x, y, w, z in zip(nums, nums[1:], nums[2:], nums[3:]):
        if (x % 2 == 0 and y % 2 != 0 and w % 2 == 0 and z % 2 != 0) or (x % 2 != 0 and y % 2 == 0 and w % 2 != 0 and z % 2 == 0):
            if x % de == 0 or y % de == 0 or w % de == 0 or z % de == 0:
                count += 1
                maxi = max(maxi, x + y + w + z)
    print(count, maxi)
