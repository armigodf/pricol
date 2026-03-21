with open('17 (2).txt') as f:
    nums = [int(num) for num in f]
    count = 0
    podh = []
    for x, y in zip(nums, nums[1:]):
        if (x % 2 == 0 and y % 2 == 0) and ((x + y) > max(nums)):
            count += 1
            podh.append(x + y)
    print(count, max(podh))
