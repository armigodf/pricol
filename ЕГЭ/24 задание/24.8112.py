from re import findall
with open('24.8112.txt') as f:
    s = f.readline()
    maxi = 0
    pattern = r'(?:[8][0-9ABCDEF]*)'
    res = findall(pattern, s)
    for i in res:
        if int(i, 16) % 8 == 0:
            maxi = max(maxi, len(i))
    print(maxi)



# with open('demo_2025_24 (1).txt') as f:
#     s = f.readline()
#     pattern = r'(?:0|[6789][06789]*)(?:[*-](?:0|[6789][06789]*))*'
#     a = findall(pattern, s)
#     max_len = max(a, key=len)
#     print(len(max_len))