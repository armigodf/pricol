from ipaddress import ip_network

net = ip_network('228.172.236.0/255.255.240.0', strict=False)
count = 0
for ip in net:
    ip_bin = bin(int(ip))[2:]
    if ip_bin.count('1') % 5 != 0:
        count += 1
print(count)
