def determinate(points):
    d1 = d2 = 0
    for i in range(len(points) - 1):
        d1 += points[i][0] * points[i + 1][1]
        d2 += points[i][1] * points[i + 1][0]
    return d1 - d2


n = int(input())
while n > 0:
    data = [int(data) for data in input().split(" ")]
    points = []
    numPoints = data.pop(0)
    for i in range(0, numPoints * 2, 2):
        points.append([data[i], data[i + 1]])
    points.append([data[0], data[1]])
    print(0.5 * determinate(points))
    n -= 1
