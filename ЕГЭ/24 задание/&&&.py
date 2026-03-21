from re import findall

with open('&&&.txt') as f:
    s = f.readline()
    pattern = r'(?:[1][0]*)(?:[&|](?:[1][0]*))*'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))
