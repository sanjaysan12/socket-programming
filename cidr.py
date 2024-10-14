from netaddr import IPNetwork
for ip in IPNetwork('172.30.16.104/16'):
    print(f"{ip} : free")