from ipaddress import ip_network


# net = ip_network('172.16.168.0/255.255.248.0', strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 5 != 0:
#         count += 1
# print(count)


# net = ip_network('210.102.240.138/255.255.255.224', strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 6 != 0:
#         count += 1
# print(count)


# net = ip_network('172.30.0.0/255.254.0.0', strict= False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 12 != 0:
#         count += 1
# print(count)


# net = ip_network('10.112.0.0/255.248.0.0', strict= False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 3 == 0:
#         count += 1
# print(count)


# net = ip_network('17.227.57.151/255.254.0.0', strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 3 == 0:
#         count += 1
# print(count)


# net = ip_network('172.224.244.176/255.255.255.240', strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 2 == 0:
#         count += 1
# print(count)


# net = ip_network('142.124.0.0/255.255.0.0', strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') <= 18:
#         count += 1
# print(count)


# net = ip_network('128.0.0.0/255.248.0.0', strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') == 16:
#         count += 1
# print(count)


# ip_bin = bin(63)[2:]
# print(ip_bin)
# num = bin(32)[-5:] + bin(63)[4:]
# print(int(num, 2))


# net = ip_network('142.10.32.63/255.255.128.0', strict=False)
# count = 0
# for ip in net:
#     if str(ip) == '142.10.32.63':
#         print(count)
#     count += 1


# net = ip_network("112.160.0.0/255.240.0.0", strict=False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 5 != 0:
#         count += 1
# print(count)


# net = ip_network('172.16.168.0/255.255.248.0', False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 5 != 0:
#         count += 1
# print(count)


# net = ip_network('137.214.144.176/255.255.255.252', False)
# count = 0
# for ip in net:
#     print(ip)


# net = ip_network('172.224.244.176/255.255.255.240', False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 2 == 0:
#         count += 1
# print(count)


# net = ip_network('142.124.0.0/255.255.0.0', False)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') <= 18:
#         count += 1
# print(count)


for mask in range(33):
    net = ip_network(f'84.32.84.32/{mask}', False)
    if bin(int(net[-2]))[2:].count('1') == 19:
        print(mask)
        break

# print(bin(212)[2:])
# print(int('11111100', 2))
