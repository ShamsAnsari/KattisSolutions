
while True:
    data = [float(data) for data in input().strip().split(" ")]
    if len(data) == 1 and data[0] == 0:
        break
    x1, y1, x2, y2, p = data
    d = (abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1/p)
    print("{:.11f}".format(d))
