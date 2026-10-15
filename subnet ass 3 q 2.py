import ipaddress
import math
ip = input("Enter ip address ")
subnets = int(input("Enter no of subnets "))
first = int(ip.split('.')[0])

if 1 <= first <= 126:
    default_prefix = 8
elif 128 <= first <= 191:
    default_prefix = 16
elif 192 <= first <= 223:
    default_prefix = 24
else:
    print("Invalid IP address ")

borrowed_bits = math.ceil(math.log2(subnets))
new_prefix = default_prefix + borrowed_bits

if(new_prefix > 30):
    print("No of subnets can't be created ")
else:
    mask = str(ipaddress.IPv4Network("0.0.0.0/"+str(new_prefix)).netmask)

print("IP address ", ip)
print("Subnets ", subnets)
print("Subnet mask ", mask)
