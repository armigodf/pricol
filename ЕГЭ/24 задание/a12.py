with open('a12.txt') as f:
    s = f.readlines()
    nums = [num for num in s]
    maxi = 0
    for i in range(len(s)):
        if nums[i].count('F') < 48 and nums[i].count('C') <= 21:
            for j in range(len(nums[i]) - 1):
                for k in range(j + 1, len(nums[i])):
                    if nums[i][j] == nums[i][k] and abs(j - k) > maxi:
                        maxi = max(maxi, abs(j - k))
    print(maxi)
