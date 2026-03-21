from re import findall
with open('21421.txt') as f:
    s = f.readline()
    pattern = r'(?:0|([1-9AB][0-9AB]*[02468A]))'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))
