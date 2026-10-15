FLAG = "0111110"

def stuff(data):
    result = ""
    count = 0

    for bit in data:
        result += bit

        if(bit == '1'):
            count += 1

            if(count == 5):
                result += '0'
                count = 0
        else:
            count = 0

    return FLAG + result + FLAG

def destuff(data):
    data = data[len(FLAG):-len(FLAG)]
    result = ""
    count = 0
    i = 0

    while i < len(data):
        bit  = data[i]
        result += bit
        if(bit == '1'):
            count += 1

            if(count == 5):
                if i + 1 < len(data) and data[i + 1] == '0':
                    i += 1
                count = 0
        else:
            count = 0
        i += 1

    return result

data = input("Enter binary data ")
stuffed = stuff(data)
destuffed = destuff(data)

print("Stuffed data : ", stuffed)
print("Destuffed data : ", destuffed)