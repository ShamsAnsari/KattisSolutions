"""
1. When you leave, always leave the seat up

2. When you leave, always leave the seat down

3. When you leave, always leave the seat as you would like to find it
"""
data = input()

case_1 = 0
case_2 = 0
case_3 = 0

if data[0] == "U":
    if data[1] == "U":
        case_2 += 1
    else:# data[1] == "D"
        case_1 += 2
        case_2 += 1
        case_3 += 1
else:# data[0] == "D"
    if data[1] == "U":
        case_1 += 1
        case_2 += 2
        case_3 += 1
    else:# data[1] == "D"
        case_1 += 1



for i in range(2, len(data)):
    if data[i] == "U":
        case_2 += 2
        if data[i - 1] == "D":
            case_3 += 1
    else: # data[i] == "D"
        case_1 += 2
        if data[i - 1] == "U":
            case_3 += 1

print(case_1)
print(case_2)
print(case_3)
