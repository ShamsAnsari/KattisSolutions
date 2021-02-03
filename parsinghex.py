# 0-9: 48-57
# A-B: 65-90
# a-b: 97-122
def isHexNum(char):
    if not(char.isalnum() or char.isdigit()):
        return False
    n = ord(char)
    return (48 <= n <= 57) or (65 <= n <= 70) or (97 <= n <= 102)


def getHex(line, i):
    hex = line[i: i + 2]
    index = i + 2
    for j in range(8):
        if i + j + 2 >= len(line):
            break
        if isHexNum(line[i + j + 2]):
            index += 1
            hex += line[i + j + 2]
        else:
            break
    return hex, index
try:
    while True:
        line = input().rstrip()
        hex = ""
        for i in range(len(line) - 2):
            if line[i] == '0' and line[i + 1].lower() == 'x' and isHexNum(line[i+2]):
                hex, i = getHex(line, i)
                if hex.lower() != "0x":
                    print(str(hex) + " " + str(int(hex, 0)))
        if line == "":
            break
except EOFError:
    pass
