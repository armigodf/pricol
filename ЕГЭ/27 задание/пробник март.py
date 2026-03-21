N = 1086
count = 0
f = open('пробник март-A.txt')
s = f.readlines()
for i in range(1, len(s)):
    for j in range(i, len(s)):
        if j - i + 1 >= 14:
            if (int(s[i]) + int(s[j])) % 8 == 0 and (int(s[i]) * int(s[j])) % 19683 == 0:
                count += 1
print(count)