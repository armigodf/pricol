from fnmatch import *


for x in range(29, 10**7, 29):
    if fnmatch(str(x), '4*217?3'):
        print(x, x // 29)