from fnmatch import *
for x in range(77, 10**7, 77):
    if fnmatch(str(x), '1*343?1'):
        print(x)