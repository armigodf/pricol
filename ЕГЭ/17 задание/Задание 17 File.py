with open('file.txt.txt') as f:
    podh = []
    nums = [int(num) for num in f]
    for i in range(len(nums) - 1):
        if ((nums[i] % 7 == 0) or (nums[i + 1] % 7 == 0)) and \
        ((abs(nums[i]) % 10 == 3) or (abs(nums[i + 1]) % 10 == 3)):
            podh.append(nums[i] + nums[i + 1])
print(len(podh))
print(max(podh))
