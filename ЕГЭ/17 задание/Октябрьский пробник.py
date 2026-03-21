with open('17 (1).txt') as f:
    num = list(map(int, f.read().split()))

count = 0
max_sum = 0

for i in range(len(num) - 4):
    if num[i] % 5 == 0 and all(num % 5 != 0 for num in num[i + 1:i + 5]) and sum(num[i:i + 5]) % 3 == 1:
        count += 1
        max_sum = max(max_sum, sum(num[i:i+5]))

print(count, max_sum)
