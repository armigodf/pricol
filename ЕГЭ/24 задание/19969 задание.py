from re import findall

with open('24_19969.txt') as f:
    s = f.readline()
    patern = r'(?:[a-z]*)(?:@)(?:[a-z]*)(?:\.)(?:[a-z]*)'
    a = findall(patern, s)
    max_len = max(a, key=len)
    print(len(max_len))
