from ipaddress import ip_network

for m in range(33):
    n = ip_network(f'29.148.33.202/{m}', 0)
    print(n)