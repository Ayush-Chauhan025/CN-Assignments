ip = input("Enter the ip address \n")

def validate(address):
    octate = address.split('.')
    n = len(octate)
    if(n != 4): return False
    for part in octate:
        if(len(part) == 0 or len(part) > 3 or (len(part) > 1 and part[0]  == '0')):
            return False
        for ch in part:
            if(not (ch >= '0' and ch <= '9')):
                return False
        if(int(part) > 255 or int(part) < 0):
            return False
    return True

def convert_2_32bit(address):
    octate = address.split('.')
    binary = []
    for part in octate:
        s = ""
        num = int(part)
        for bit in range(7, -1, -1):
            if((num & (1 << bit) != 0)): s += '1'
            else: s += '0'
        binary.append(s)
    converted_ip = ".".join(binary)
    print(converted_ip)

valid = validate(ip)
if(valid): convert_2_32bit(ip)
else: print("invalid address")