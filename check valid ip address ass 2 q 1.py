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

def get_class(address):
    octate = address.split('.')
    val = int(octate[0])
    if 1 <= val <= 126:
        print("Class A")
    elif 127 <= val <= 191:
        print("Class B")
    elif 192 <= val <= 223:
        print("Class C")
    elif 224 <= val <= 239:
        print("Class D")
    else:
        print("Class E")

valid = validate(ip)
if(valid): get_class(ip)
else: print("Invalid address")