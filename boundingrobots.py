def addSteps(dir, len, w, l, rx, ry, ax, ay):
    if dir == 'u':
        ry += len
        ay += len
        if ay >= l - 1:
            ay = l - 1
    elif dir == 'd':
        ry -= len
        ay -= len
        if ay < 0:
            ay = 0
    elif dir == 'r':
        rx += len
        ax += len
        if ax >= w - 1:
            ax = w - 1
    elif dir == 'l':
        rx -= len
        ax -= len
        if ax < 0:
            ax = 0
    return rx, ry, ax, ay



while True:
    dimensions = [int(inpt) for inpt in input().strip().split(" ")]
    (w, l) = (dimensions[0], dimensions[1])
    if w == 0 or l == 0:
        break
    (ax, ay) = (0, 0)
    (rx, ry) = (0, 0)

    numSteps = int(input())
    for i in range(numSteps):
        steps = input().strip().split(" ")
        steps[1] = int(steps[1])
        rx, ry, ax, ay = addSteps(steps[0], steps[1], w, l, rx, ry,ax,ay)
    print("Robot thinks " + str(rx) + " " + str(ry))
    print("Actually at " + str(ax) + " " + str(ay))
