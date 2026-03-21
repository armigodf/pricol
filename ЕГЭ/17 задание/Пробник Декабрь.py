with open('Пробник Декабрь.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    for x in range(len(nums) - 1):
        for y in range(x + 1, len(nums)):
            if (nums[x] + nums[y]) % 12 == 0:
                count += 1
                maxi = max(maxi, nums[x] + nums[y])
    print(count, maxi)
