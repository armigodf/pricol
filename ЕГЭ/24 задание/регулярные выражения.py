from re import findall
with open('demo_2025_24 (1).txt') as f:
    s = f.readline()
    pattern = r'(?:0|[6789][06789]*)(?:[*-](?:0|[6789][06789]*))*'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))



