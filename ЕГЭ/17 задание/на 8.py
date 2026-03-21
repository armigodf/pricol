with open('на 8.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    mini = 11111
    for x, y in zip(nums, nums[1:]):
        if x % 11 == 0 and y % 11 == 0:
            if abs(x) % 10 == 8 or abs(y) % 10 == 8:
                count += 1
                mini = min(mini, x + y)
    print(count, mini)
