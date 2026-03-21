from re import findall

with open('regular.txt') as f:
    s = f.readline()
    pattern = r'[1-9A-D][0-9A-D]*[02468AC]'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))
















    # s = f.readline()
    # pattern = r'(?:0|[6789][06789]*)(?:[*-](?:0|[6789][06789]*))*'
    # a = findall(pattern, s)
    # max_len = max(a, key=len)
    # print(len(max_len))