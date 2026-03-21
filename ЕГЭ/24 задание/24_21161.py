from re import findall
with open('24_21161.py') as f:
    s = f.readline()
    pattern = r'[ABC][abc]*(?: [ABCabc][abc]*)*\.'
    a = findall(pattern, s)
    max_len = max(a, key=len)
    print(len(max_len))
