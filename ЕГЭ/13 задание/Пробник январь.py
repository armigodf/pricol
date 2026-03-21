from ipaddress import *
net = ip_network('192.166.133.96/255.255.255.224', strict=False)

count = 0
for ip in net:
    if str(ip)[-1] == '6':
        count += 1
print(count)
