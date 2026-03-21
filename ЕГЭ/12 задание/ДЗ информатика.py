# s = '3' * 160
# while ('333' in s) or ('11' in s):
#     if '333' in s:
#         s = s.replace('333', '1', 1)
#     if '11' in s:
#         s = s.replace('11', '3', 1)
# print(s)


s = '9' * 122
while ('9999' in s) or ('12' in s):
    if ('9999' in s):
        s = s.replace('9999', '112', 1)
    if ('12' in s):
        s = s.replace('12', '9', 1)
print(s)
