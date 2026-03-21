# with open('21342439673613d75f8f35.46625806172.txt') as f:
#     count = 0
#     podh = []
#     nums = [int(num) for num in f]
#     min_seven = min(nums) % 7
#     max_three = max(nums) % 3
#     for x, y in zip(nums, nums[1:]):
#         if (((x % 3 == max_three) + (y % 3 == max_three)) >= 1) and \
#         (((y % 7 == min_seven) + (x % 7 == min_seven)) >= 1):
#             count += 1
#             podh.append((x + y))
#     print(count)
#     print(max(podh))


