from re import findall
with open('CF38C4.txt') as f:
    s = f.readline()
    patern = r'(?:0|[2345][02345]*)(?:[*-](?:0|[2345][02345]*))*'
    numbers = findall(patern, s)
    max_len = max(numbers, key=len)
    print(len(max_len))
