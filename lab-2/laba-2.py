def gsd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gsd(588, 108))