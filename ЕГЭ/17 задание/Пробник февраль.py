with open('Пробник Февраль.txt') as f:
    nums = [int(num) for num in f]
    count = 0
    maxi = -1
    for x, y in zip(nums, nums[1:]):
        if (x % 8 == 0 or y % 8 == 0) and (((x * y) % 3) == 0):
            count += 1
            if x + y > maxi:
                maxi = x + y
    print(count, maxi)
    