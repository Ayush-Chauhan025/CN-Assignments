ip = input("Enter IP ")
first = int(ip.split('.'))
if 1 <= first <= 126:
    print("Default subnet mask: 255.0.0.0")
elif 128 <= first <= 191:
    print("Default subnet mask: 255.255.0.0")
elif 192 <= first <= 223:
    print("Default subnet mask: 255.255.255.0")
elif 224 <= first <= 239:
    print("Class D, No Default Subnet Mask")
elif 240 <= first <= 255:
    print("Class E, No Default Subnet Mask")
else:
    print("Invalid IP")