from re import findall
with open('24_21908.txt') as f:
    s = f.readline()
    pattern = r'(?:0|[1-9ABCD][0-9ABCD]*[02468AC])'
    a = findall(pattern, s)
    max_len = max(a, key=lambda x: int(x, 14))
    print(len(max_len))
