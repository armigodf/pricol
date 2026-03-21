from ipaddress import ip_network

net = ip_network('172.224.244.176/255.255.255.240', False)
count = 0
for i in net:
    if (bin(int(i))[2:].count('1')) % 2 == 0:
        count += 1
print(count)
