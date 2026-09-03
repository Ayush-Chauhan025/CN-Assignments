FLAG = '#'
ESC = '/'

def stuff(data):
    result = FLAG

    for char in data:
        if char == FLAG or char == ESC:
            result += ESC
        result += char
    result += FLAG
    return result

def destuff(data):
    data = data[1:-1]
    result = ""
    i = 0

    while i < len(data):
        if data[i] == ESC:
            i += 1

        result += data[i]
        i += 1

    return result

data = input("Enter binary data ")
stuffed = stuff(data)
destuffed = destuff(data)

print("Stuffed data : ", stuffed)
print("Destuffed data : ", destuffed)