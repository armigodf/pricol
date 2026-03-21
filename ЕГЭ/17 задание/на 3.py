with open('на 3.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = 0
    for x, y in zip(nums, nums[1:]):
        if x % 7 == 0 or y % 7 == 0:
            if abs(x) % 10 == 3 or abs(y) % 10 == 3:
                count += 1
                maxi = max(maxi, x + y)
    print(count, maxi)
