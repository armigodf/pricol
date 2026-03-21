with open('фаил.1.txt') as f:
    nums = [int(num) for num in f]
    mini3 = min([i for i in nums if (i % 10 == 5) and (99 < i < 1000)])
    count = 0
    maxi = 0
    for x, y in zip(nums, nums[1:]):
        if (99 < x < 1000) or (99 < y < 1000):
            if (x + y) % mini3 == 0:
                count += 1
                maxi = max(maxi, x + y)
    print(count, maxi)
