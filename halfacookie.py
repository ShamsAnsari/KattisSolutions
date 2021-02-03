import math

data = []
try:
    while True:
        line = input()
        if line == '':
            break
        data.append([float(datum) for datum in line.strip().split(" ")])

except EOFError:
    pass

for datum in data:
    R = datum[0]
    (x, y) = (datum[1], datum[2])
    areaCircle = math.pi * R ** 2
    d = math.sqrt((x ** 2) + (y ** 2))
    if d >= R:
        print("miss")
        continue
    areaSegment = R * (R * math.acos(d / R) - d * math.sqrt(1 - (d / R) ** 2))
    areaSegment2 = areaCircle - areaSegment
    if areaSegment2 > areaSegment:
        print(str(areaSegment2) + " " + str(areaSegment))
    else:
        print(str(areaSegment2) + " " + str(areaSegment))
