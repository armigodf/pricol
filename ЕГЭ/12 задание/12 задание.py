# s = '252' * 5
# while ('2222' in s) or ('55' in s):
#     if '2222' in s:
#         s = s.replace('2222', '5', 1)
#     else:
#         s = s.replace('55', '2', 1)
# print(s)


# s = '1' * 77
# while '11' in s:
#     s = s.replace('222', '1', 1)
#     s = s.replace('11', '2', 1)
#     print(s)


# s = '1' * 102
# while '111' in s:
#     s = s.replace('111', '22', 1)
#     s = s.replace('222', '11', 1)
# print(s)


# s = '1' * 84
# while '11111' in s:
#     s = s.replace('222', '2', 1)
#     s = s.replace('111', '2', 1)
#     print(s)


# s = '1' * 40 + '2' * 40
# while '111' in s:
#     s = s.replace('111', '2', 1)
#     s = s.replace('222', '1', 1)
#     print(s)


# s = '1' + '8' * 99 + '1'
# while ('81' in s) or ('882' in s) or ('8883' in s):
#     if '81' in s:
#         s = s.replace('81', '2', 1)
#     elif '882' in s:
#         s = s.replace('882', '3', 1)
#     else:
#         s = s.replace('8883', '1', 1)
# print(s)


# s = 129 * '2'
# while ('222' in s) or ('4444' in s):
#     if '222' in s:
#         s = s.replace('222', '44', 1)
#     else:
#         s = s.replace('4444', '2', 1)
# print(s)


s = '1' * 99
while ('111' in s) or ('222' in s):
    if '111' in s:
        s = s.replace('111', '22', 1)
    if '222' in s:
        s = s.replace('222', '1', 1)
print(s)
