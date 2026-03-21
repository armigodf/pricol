from re import findall

with open('1230.txt') as f:
    s = f.readline()
    pattern = r'(?:[123][0123]*)(?:[*+](?:[123][0123]*))*'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))
    