with open('пробник апрель.txt') as f:
    nums = f.readline().replace('BCA', 'BC_CA').split('_')
    maxi = 0
    for i in range(len(nums)):
        if len(nums[i]) > maxi:
            maxi = len(nums[i])
    print(maxi)

