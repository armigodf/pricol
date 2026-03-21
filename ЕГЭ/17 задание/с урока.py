with open('с урока.txt') as f:
    nums = [int(num) for num in f]
    maxi = 0
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) % 58 == 0:
                count += 1
                maxi = max(maxi, (nums[i] + nums[j]))
    print(count, maxi)
