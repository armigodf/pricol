from re import findall
with open('20813.txt') as f:
    s = f.readline()
    pattern = r'(?:0|[789][0789]*)(?:[*-](?:0|[789][0789]*))*'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))
