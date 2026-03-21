from fnmatch import *

for i in range(25047, 10**10 + 1, 25047):
    if fnmatch(str(i), '1?6?2*6'):
        print(i, i // 25047)

